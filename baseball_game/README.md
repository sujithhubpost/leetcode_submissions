

# [682\. Baseball Game](https://leetcode.com/problems/baseball-game/submissions/)



Easy

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings `ops`, where `ops[i]` is the `ith` operation you must apply to the record and is one of the following:

1.  An integer `x` - Record a new score of `x`.
2.  `"+"` - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
3.  `"D"` - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
4.  `"C"` - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.

Return _the sum of all the scores on the record_.

**Example 1:**

**Input:** ops = \["5","2","C","D","+"\]

**Output:** 30

**Explanation:**
"5" - Add 5 to the record, record is now \[5\].

"2" - Add 2 to the record, record is now \[5, 2\].

"C" - Invalidate and remove the previous score, record is now \[5\].

"D" - Add 2 \* 5 = 10 to the record, record is now \[5, 10\].

"+" - Add 5 + 10 = 15 to the record, record is now \[5, 10, 15\].
The total sum is 5 + 10 + 15 = 30.

**Example 2:**

**Input:** ops = \["5","-2","4","C","D","9","+","+"\]

**Output:** 27

**Explanation:**
"5" - Add 5 to the record, record is now \[5\].

"-2" - Add -2 to the record, record is now \[5, -2\].

"4" - Add 4 to the record, record is now \[5, -2, 4\].

"C" - Invalidate and remove the previous score, record is now \[5, -2\].

"D" - Add 2 \* -2 = -4 to the record, record is now \[5, -2, -4\].

"9" - Add 9 to the record, record is now \[5, -2, -4, 9\].

"+" - Add -4 + 9 = 5 to the record, record is now \[5, -2, -4, 9, 5\].

"+" - Add 9 + 5 = 14 to the record, record is now \[5, -2, -4, 9, 5, 14\].

The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

**Example 3:**

**Input:** ops = \["1"\]

**Output:** 1

**Constraints:**

*   `1 <= ops.length <= 1000`
*   `ops[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 104, 3 * 104]`.
*   For operation `"+"`, there will always be at least two previous scores on the record.
*   For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

Accepted

176,432

<div data-key="submissions-content" data-cy="submissions-content" class="tab-pane__ncJk css-1eusa4c-TabContent e5i1odf5">

<div class="container__hnR0 container__3BF-">

<div class="submissions__1ROo">

<div class="result-container__33Nb">

<div class="container__nthg">

<div class="result__23wN">

<div class="success__3Ai7">Success</div>

[Details](/submissions/detail/677715047/)</div>

<div class="info__2oQ9"><span>Runtime: <span class="data__HC-i">47 ms</span><span>, faster than <span class="data__HC-i">73.95%</span> of Python3 online submissions for Baseball Game.</span></span></div>

<div class="info__2oQ9"><span>Memory Usage: <span class="data__HC-i">14.1 MB</span><span>, less than <span class="data__HC-i">34.49%</span> of Python3 online submissions for Baseball Game.</span></span></div>





</div>

<div class="addl-success-info__2ySC">



</div>

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

<tr class="ant-table-row ant-table-row-level-0" data-row-key="677715047">

<td class="time-column__1guG">04/10/2022 21:24</td>

<td class="status-column__3SUg">[Accepted](/submissions/detail/677715047/)</td>

<td class="runtime-column__1ka_">47 ms</td>

<td class="memory-column__1dxp">14.1 MB</td>

<td class="lang-column__tR-8">python3</td>

</tr>

<tr class="ant-table-row ant-table-row-level-0" data-row-key="677703968">

<td class="time-column__1guG">04/10/2022 21:02</td>

<td class="status-column__3SUg">[Accepted](/submissions/detail/677703968/)</td>

<td class="runtime-column__1ka_">88 ms</td>

<td class="memory-column__1dxp">14.2 MB</td>

<td class="lang-column__tR-8">python3</td>

</tr>

<tr class="ant-table-row ant-table-row-level-0" data-row-key="677703816">

<td class="time-column__1guG">04/10/2022 21:01</td>

<td class="status-column__3SUg">[Compile Error](/submissions/detail/677703816/)</td>

<td class="runtime-column__1ka_">N/A</td>

<td class="memory-column__1dxp">N/A</td>

<td class="lang-column__tR-8">cpp</td>

</tr>

</tbody>

</table>
