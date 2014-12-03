--local exports = {}

function update_password(rec, new_password)
  -- Log current password
  warn("Old pwd for %s is %s", rec['username'], rec['password']);
  -- Assign new password to the user record
  rec['password'] = new_password
  -- Log new password
  warn("New pwd for %s is %s", rec['username'], rec['password']);
  --warn("New pwd for %s is %s", rec['username'], rec['password']);
  -- Update user record
  aerospike:update(rec)
  -- Return new password
  --return rec['password']
  return 0
end

local function aggregate_stats(map,rec)
  -- Exercise 1
  -- NOTE: rec will include 'region' bin of type string and the valid values are 'n', 's', 'e', 'w'
  -- Examine value of 'region' bin in record rec and increment respective counter in the map
  local region = rec['region']
  map[region] = (map[region] or 0) + 1
  -- Return updated map
  warn("map = n:%s s:%s e:%s w:%s region:%s", map['n'], map['s'], map['e'], map['w'], rec['region'])
  return map
end

local function reduce_stats(a,b)
  -- Merge values from map b into a
  a.n = a.n + b.n
  a.s = a.s + b.s
  a.e = a.e + b.e
  a.w = a.w + b.w
  -- Return updated map a
  warn("a = n:%s s:%s e:%s w:%s", a.n, a.s, a.e, a.w);
  return a
end

function sum(stream)
  -- Exercise 1
  -- Process incoming record stream and pass it to aggregate function, then to reduce function
  --   NOTE: aggregate function aggregate_stats accepts two parameters: 
  --    1) A map that contains four variables to store number-of-users counter for north, south, east and west regions with initial value set to 0  
  --    2) function name aggregate_stats -- which will be called for each record as it flows in
  -- Return reduced value of the map generated by reduce function reduce_stats
  return stream : aggregate(map{n=0,s=0,e=0,w=0}, aggregate_stats) : reduce(reduce_stats);
end

