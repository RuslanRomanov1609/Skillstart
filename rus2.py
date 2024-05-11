<html>
<head>
<title>rus2.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #6aab73;}
.s4 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
rus2.py</font>
</center></td></tr></table>
<pre><span class="s0">def </span><span class="s1">my_decor</span><span class="s2">(</span><span class="s1">func</span><span class="s2">):</span>
    <span class="s0">def </span><span class="s1">wrapper</span><span class="s2">(</span><span class="s1">n</span><span class="s2">):</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s3">'start'</span><span class="s2">)</span>
        <span class="s1">func</span><span class="s2">(</span><span class="s1">n</span><span class="s2">)</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s3">'end'</span><span class="s2">)</span>
    <span class="s0">return </span><span class="s1">wrapper</span>
<span class="s2">@</span><span class="s1">my_decor</span>
<span class="s0">def </span><span class="s1">my_func</span><span class="s2">(</span><span class="s1">number</span><span class="s2">):</span>
    <span class="s1">print</span><span class="s2">(</span><span class="s1">number</span><span class="s2">**</span><span class="s4">2</span><span class="s2">)</span>
<span class="s1">my_func</span><span class="s2">(</span><span class="s4">10</span><span class="s2">)</span>













































</pre>
</body>
</html>