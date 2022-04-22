# Problem Statement

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

*   `MyHashMap()` initializes the object with an empty map.
*   `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
*   `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
*   `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

**Example 1:**

<pre>**Input**
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
**Output**
[null, null, null, 1, -1, null, 1, null, -1]

**Explanation**
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
</pre>

**Constraints:**

*   `0 <= key, value <= 10<sup>6</sup>`
*   At most `10<sup>4</sup>` calls will be made to `put`, `get`, and `remove`.

<br>

# Solution

<div class="success__3Ai7">Success</div>


<div class="info__2oQ9"><span>Runtime: <span class="data__HC-i">231 ms</span><span>, faster than <span class="data__HC-i">91.72%</span> of Python3 online submissions for Design HashMap.</span></span></div>
<br>
<div class="info__2oQ9"><span>Memory Usage: <span class="data__HC-i">17.2 MB</span><span>, less than <span class="data__HC-i">83.70%</span> of Python3 online submissions for Design HashMap.</span></span></div>



<table class="">

<thead class="ant-table-thead">

<tr>

<th class="time-column__1guG"><span class="ant-table-header-column">

<div><span class="ant-table-column-title">Time Submitted</span><span class="ant-table-column-sorter"></span></div>

</span></th>

<th class="status-column__3SUg"><span class="ant-table-header-column">

<div><span class="ant-table-column-title">Status</span><span class="ant-table-column-sorter"></span></div>

</span></th>

<th class="runtime-column__1ka_"><span class="ant-table-header-column">

<div><span class="ant-table-column-title">Runtime</span><span class="ant-table-column-sorter"></span></div>

</span></th>

<th class="memory-column__1dxp"><span class="ant-table-header-column">

<div><span class="ant-table-column-title">Memory</span><span class="ant-table-column-sorter"></span></div>

</span></th>

<th class="lang-column__tR-8"><span class="ant-table-header-column">

<div><span class="ant-table-column-title">Language</span><span class="ant-table-column-sorter"></span></div>

</span></th>

</tr>

</thead>

<tbody class="ant-table-tbody">

<tr class="ant-table-row ant-table-row-level-0" data-row-key="685534585">

<td class="time-column__1guG">04/22/2022 23:04</td>

<td class="status-column__3SUg">[Accepted](/submissions/detail/685534585/)</td>

<td class="runtime-column__1ka_">231 ms</td>

<td class="memory-column__1dxp">17.2 MB</td>

<td class="lang-column__tR-8">python3</td>

</tr>

<tr class="ant-table-row ant-table-row-level-0" data-row-key="685533491">

<td class="time-column__1guG">04/22/2022 23:02</td>

<td class="status-column__3SUg">[Wrong Answer](/submissions/detail/685533491/)</td>

<td class="runtime-column__1ka_">N/A</td>

<td class="memory-column__1dxp">N/A</td>

<td class="lang-column__tR-8">python3</td>

</tr>

<tr class="ant-table-row ant-table-row-level-0" data-row-key="685530762">

<td class="time-column__1guG">04/22/2022 22:57</td>

<td class="status-column__3SUg">[Runtime Error](/submissions/detail/685530762/)</td>

<td class="runtime-column__1ka_">N/A</td>

<td class="memory-column__1dxp">N/A</td>

<td class="lang-column__tR-8">python3</td>

</tr>

</tbody>

</table>
