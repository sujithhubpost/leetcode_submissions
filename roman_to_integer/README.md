# Problem

<div data-key="description-content" data-cy="description-content" class="tab-pane__ncJk css-1eusa4c-TabContent e5i1odf5">

<div class="description__24sA">

<div class="css-101rr4k">

<div data-cy="question-title" class="css-v3d350">13. Roman to Integer</div>

<br>

<div diff="easy" class="css-14oi08n">Easy</div>

</div>

</div>

<div class="content__u3I1 question-content__JfgR">

<div>

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

<pre>**Symbol**       **Value**
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

*   `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
*   `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
*   `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

<pre>**Input:** s = "III"
**Output:** 3
**Explanation:** III = 3.
</pre>

**Example 2:**

<pre>**Input:** s = "LVIII"
**Output:** 58
**Explanation:** L = 50, V= 5, III = 3.
</pre>

**Example 3:**

<pre>**Input:** s = "MCMXCIV"
**Output:** 1994
**Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

**Constraints:**

*   `1 <= s.length <= 15`
*   `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
*   It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

</div>

</div>

# Submission


<div class="info__2oQ9"><span>Runtime: <span class="data__HC-i">108 ms</span><span>, faster than <span class="data__HC-i">6.40%</span> of Python3 online submissions for Roman to Integer.</span></span></div>

<div class="info__2oQ9"><span>Memory Usage: <span class="data__HC-i">13.8 MB</span><span>, less than <span class="data__HC-i">80.57%</span> of Python3 online submissions for Roman to Integer.</span></span></div>

<br>

<table class=""><colgroup><col><col><col><col><col></colgroup>

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

<tr class="ant-table-row ant-table-row-level-0" data-row-key="678545327">

<td class="time-column__1guG">04/12/2022 02:11</td>

<td class="status-column__3SUg">[Accepted](/submissions/detail/678545327/)</td>

<td class="runtime-column__1ka_">108 ms</td>

<td class="memory-column__1dxp">13.8 MB</td>

<td class="lang-column__tR-8">python3</td>

</tr>

<tr class="ant-table-row ant-table-row-level-0" data-row-key="678479758">

<td class="time-column__1guG">04/12/2022 00:05</td>

<td class="status-column__3SUg">[Wrong Answer](/submissions/detail/678479758/)</td>

<td class="runtime-column__1ka_">N/A</td>

<td class="memory-column__1dxp">N/A</td>

<td class="lang-column__tR-8">python3</td>

</tr>

</tbody>

</table>
