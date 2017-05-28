import re
import pprint
import json

content = """
<td>1</td>
<td>abide<span style="color: #c0c0c0;" data-mce-mark="1"> [ə'baɪd]</span></td>
<td>abode <span style="color: #c0c0c0;" data-mce-mark="1">[ə'bəud]</span></td>
<td>abode&nbsp; <span style="color: #c0c0c0;" data-mce-mark="1">[ə'bəud]</span></td>
<td>пребывать, придерживаться чего-либо</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>2</td>
<td>arise<span style="color: #888888;" data-mce-mark="1"> <span style="color: #c0c0c0;" data-mce-mark="1">[ə'raɪz]</span></span></td>
<td>arose<span style="color: #c0c0c0;" data-mce-mark="1"> [ə'rəuz]</span></td>
<td>arisen<span style="color: #c0c0c0;" data-mce-mark="1"> [ə'rɪz(ə)n]</span></td>
<td>возникать, подниматься</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>3</td>
<td>awake<span style="color: #c0c0c0;" data-mce-mark="1"> [ə'weɪk]</span></td>
<td>awoke <span style="color: #c0c0c0;" data-mce-mark="1">[ə'wəuk]</span></td>
<td>awaked <span style="color: #c0c0c0;" data-mce-mark="1">[ə'weɪk]</span></td>
<td>будить, просыпаться</td>
</tr>
<tr class="let1 pop" style="display: table-row;">
<td>4</td>
<td>be&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bi:]</span></td>
<td>was <span style="color: #c0c0c0;" data-mce-mark="1">[wɔz]</span>; were <span style="color: #c0c0c0;" data-mce-mark="1">[wз:]</span></td>
<td>been&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bi:n]</span></td>
<td>быть, являться</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>5</td>
<td>bear <span style="color: #c0c0c0;" data-mce-mark="1">[beə]</span></td>
<td>bore <span style="color: #c0c0c0;" data-mce-mark="1">[bɔː]</span></td>
<td>born <span style="color: #c0c0c0;" data-mce-mark="1">[bɔːn]</span></td>
<td>носить, рождать&nbsp;</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>6</td>
<td>beat&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bi:t]</span></td>
<td>beat&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bi:t]</span></td>
<td>beaten<span style="color: #c0c0c0;" data-mce-mark="1">&nbsp;['bi:tn]</span></td>
<td>бить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>7</td>
<td>become<span style="color: #c0c0c0;" data-mce-mark="1"> [bi:kʌm]</span></td>
<td>became <span style="color: #c0c0c0;" data-mce-mark="1">[bi:keim]</span></td>
<td>become <span style="color: #c0c0c0;" data-mce-mark="1">[bi:kʌm]</span></td>
<td>становиться, делаться</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>8</td>
<td>befall <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'fɔːl]</span></td>
<td>befell <span style="color: #c0c0c0;" data-mce-mark="1">&nbsp;[bɪ'fel]</span></td>
<td>befallen <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'fɔːlən]</span></td>
<td>случаться</td>
</tr>
<tr class="let1 pop" style="display: table-row;">
<td>9</td>
<td>begin<span style="color: #c0c0c0;" data-mce-mark="1"> [bi'gin]</span></td>
<td>began <span style="color: #c0c0c0;" data-mce-mark="1">[bi'gæn]</span></td>
<td>begun<span style="color: #c0c0c0;" data-mce-mark="1"> [bi'gʌn]</span></td>
<td>начинать(ся)</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>10</td>
<td>behold <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'həuld]</span></td>
<td>beheld <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'held]</span></td>
<td>beheld <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'held]</span></td>
<td>вглядываться, замечать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>11</td>
<td>bend <span style="color: #c0c0c0;" data-mce-mark="1">[bend]</span></td>
<td>bent&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bent]&nbsp;</span></td>
<td>bent&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[bent] &nbsp;</span></td>
<td>гнуть(ся), сгибать(ся)</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>12</td>
<td>beseech <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'siːʧ]</span></td>
<td>besought <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'sɔːt]</span></td>
<td>besought <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'sɔːt]</span></td>
<td>умолять, упрашивать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>13</td>
<td>beset <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'set]</span></td>
<td>beset <span style="color: #c0c0c0;" data-mce-mark="1">[bɪ'set]</span></td>
<td>beset<span style="color: #c0c0c0;" data-mce-mark="1"> [bɪ'set]</span></td>
<td>окружать, осаждать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>14</td>
<td>bet <span style="color: #c0c0c0;" data-mce-mark="1">[bet]</span></td>
<td>bet <span style="color: #c0c0c0;" data-mce-mark="1">[bet]</span></td>
<td>bet <span style="color: #c0c0c0;" data-mce-mark="1">[bet]</span></td>
<td>держать пари</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>15</td>
<td>bid <span style="color: #c0c0c0;" data-mce-mark="1">[bɪd]</span></td>
<td>bid <span style="color: #c0c0c0;" data-mce-mark="1">[bɪd]</span></td>
<td>bid <span style="color: #c0c0c0;" data-mce-mark="1">[bɪd]</span></td>
<td>предлагать цену, велеть, просить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>16</td>
<td>bind<span style="color: #c0c0c0;" data-mce-mark="1"> [baɪnd]</span></td>
<td>bound<span style="color: #c0c0c0;" data-mce-mark="1"> [baund]</span></td>
<td>bound<span style="color: #c0c0c0;" data-mce-mark="1"> [baund]</span></td>
<td>связывать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>17</td>
<td>bite <span style="color: #c0c0c0;" data-mce-mark="1">[baɪt]</span></td>
<td>bit<span style="color: #c0c0c0;" data-mce-mark="1"> [bɪt]</span></td>
<td>bitten <span style="color: #c0c0c0;" data-mce-mark="1">['bɪtn]</span></td>
<td>кусать(ся)</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>18</td>
<td>bleed <span style="color: #c0c0c0;" data-mce-mark="1">[bliːd]</span></td>
<td>bled <span style="color: #c0c0c0;" data-mce-mark="1">[bled]</span></td>
<td>bled <span style="color: #c0c0c0;" data-mce-mark="1">[bled]</span></td>
<td>кровоточить, опорожнять</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>19</td>
<td>blow <span style="color: #c0c0c0;" data-mce-mark="1">[bləu]</span></td>
<td>blew <span style="color: #c0c0c0;" data-mce-mark="1">[bluː]</span></td>
<td>blown<span style="color: #c0c0c0;" data-mce-mark="1"> [bləun]</span></td>
<td>дуть</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>20</td>
<td>break <span style="color: #c0c0c0;" data-mce-mark="1">[breɪk]</span></td>
<td>broke<span style="color: #c0c0c0;" data-mce-mark="1"> [brəuk]</span></td>
<td>broken <span style="color: #c0c0c0;" data-mce-mark="1">['brəuk(ə)n]</span></td>
<td>ломать, прерывать, разбивать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>21</td>
<td>breed <span style="color: #c0c0c0;" data-mce-mark="1">[briːd]</span></td>
<td>bred <span style="color: #c0c0c0;" data-mce-mark="1">[bred]</span></td>
<td>bred <span style="color: #c0c0c0;" data-mce-mark="1">[bred]</span></td>
<td>порождать, разводить, выводить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>22</td>
<td>bring <span style="color: #c0c0c0;" data-mce-mark="1">[brɪŋ]</span></td>
<td>brought<span style="color: #c0c0c0;" data-mce-mark="1"> [brɔːt]</span></td>
<td>brought<span style="color: #c0c0c0;" data-mce-mark="1"> [brɔːt]</span></td>
<td>приносить, приводить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>23</td>
<td>broadcast <span style="color: #c0c0c0;" data-mce-mark="1">['brɔːdkɑːst]</span></td>
<td>broadcast <span style="color: #c0c0c0;" data-mce-mark="1">['brɔːdkɑːst]</span></td>
<td>broadcast<span style="color: #c0c0c0;" data-mce-mark="1"> ['brɔːdkɑːst]</span></td>
<td>вещать, распространять</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>24</td>
<td>build <span style="color: #c0c0c0;" data-mce-mark="1">[bɪld]</span></td>
<td>built <span style="color: #c0c0c0;" data-mce-mark="1">[bɪlt]</span></td>
<td>built <span style="color: #c0c0c0;" data-mce-mark="1">[bɪlt]</span></td>
<td>строить, встраивать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>25</td>
<td>burn <span style="color: #c0c0c0;" data-mce-mark="1">[bɜːn]</span></td>
<td>burnt<span style="color: #c0c0c0;" data-mce-mark="1"> [bɜːnt]</span></td>
<td>burnt <span style="color: #c0c0c0;" data-mce-mark="1">[bɜːnt]</span></td>
<td>гореть, сжигать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>26</td>
<td>burst <span style="color: #c0c0c0;" data-mce-mark="1">[bɜːst]</span></td>
<td>burst <span style="color: #c0c0c0;" data-mce-mark="1">[bɜːst]</span></td>
<td>burst <span style="color: #c0c0c0;" data-mce-mark="1">[bɜːst]</span></td>
<td>взрывать(ся)</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>27</td>
<td>buy&nbsp;<span style="color: #c0c0c0;" data-mce-mark="1">[baɪ]&nbsp;</span></td>
<td>bought <span style="color: #c0c0c0;" data-mce-mark="1">[bɔːt]</span></td>
<td>bought <span style="color: #c0c0c0;" data-mce-mark="1">[bɔːt]</span></td>
<td>покупать</td>
</tr>
<tr class="let1 pop" style="display: table-row;">
<td>28</td>
<td>can <span style="color: #c0c0c0;" data-mce-mark="1">[kæn]</span></td>
<td>could <span style="color: #c0c0c0;" data-mce-mark="1">[kud]</span></td>
<td>could<span style="color: #c0c0c0;" data-mce-mark="1"> [kud]</span></td>
<td>мочь физически</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>29</td>
<td>cast <span style="color: #c0c0c0;" data-mce-mark="1">[kɑːst]</span></td>
<td>cast <span style="color: #c0c0c0;" data-mce-mark="1">[kɑːst]</span></td>
<td>cast <span style="color: #c0c0c0;" data-mce-mark="1">[kɑːst]</span></td>
<td>бросать, лить (металл)</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>30</td>
<td>catch <span style="color: #c0c0c0;" data-mce-mark="1">[kæʧ]</span></td>
<td>caught <span style="color: #c0c0c0;" data-mce-mark="1">[kɔːt]</span></td>
<td>caught <span style="color: #c0c0c0;" data-mce-mark="1">[kɔːt]</span></td>
<td>ловить, схватывать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>31</td>
<td>choose <span style="color: #c0c0c0;" data-mce-mark="1">[ʧuːz]</span></td>
<td>chose <span style="color: #c0c0c0;" data-mce-mark="1">[ʧuːz]</span></td>
<td>chosen <span style="color: #c0c0c0;" data-mce-mark="1">['ʧəuz(ə)n]</span></td>
<td>выбирать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>32</td>
<td>cling <span style="color: #c0c0c0;" data-mce-mark="1">[klɪŋ]</span></td>
<td>clung <span style="color: #c0c0c0;" data-mce-mark="1">[klʌŋ]</span></td>
<td>clung <span style="color: #c0c0c0;" data-mce-mark="1">[klʌŋ]</span></td>
<td>прилипать, цеплять, льнуть</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>33</td>
<td>cleave <span style="color: #c0c0c0;" data-mce-mark="1">[kliːv]</span></td>
<td>cleft <span style="color: #c0c0c0;" data-mce-mark="1">[kleft]</span></td>
<td>cloven <span style="color: #c0c0c0;" data-mce-mark="1">['kləuv(ə)n]</span></td>
<td>рассечь, расколоть</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>34</td>
<td>clothe <span style="color: #c0c0c0;" data-mce-mark="1">[kləuð]</span></td>
<td>clothed <span style="color: #c0c0c0;" data-mce-mark="1">[kləʊðd]</span></td>
<td>clothed <span style="color: #c0c0c0;" data-mce-mark="1">[kləʊðd]</span></td>
<td>одеть, одевать</td>
</tr>
<tr class="let1 pop" style="display: table-row;">
<td>35</td>
<td>come <span style="color: #c0c0c0;" data-mce-mark="1">[kʌm]</span></td>
<td>came <span style="color: #c0c0c0;" data-mce-mark="1">[keɪm]</span></td>
<td>come <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">kʌm</span>]</span></td>
<td>приходить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>36</td>
<td>cost <span style="color: #c0c0c0;" data-mce-mark="1">[kɒst]</span></td>
<td>cost <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">kɒst</span>]</span></td>
<td>cost <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">kɒst</span>]</span></td>
<td>оценивать, стоить</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>37</td>
<td>creep <span style="color: #c0c0c0;" data-mce-mark="1">[kriːp]</span></td>
<td>crept <span style="color: #c0c0c0;" data-mce-mark="1">[krept]</span></td>
<td>crept <span style="color: #c0c0c0;" data-mce-mark="1">[krept]</span></td>
<td>ползать</td>
</tr>
<tr class="let1" style="display: table-row;">
<td>38</td>
<td>cut <span style="color: #c0c0c0;" data-mce-mark="1">[kʌt]</span></td>
<td>cut <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">kʌt</span>]</span></td>
<td>cut <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">kʌt</span>]</span></td>
<td>резать, обрезать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>39</td>
<td>dare <span style="color: #c0c0c0;" data-mce-mark="1">[deə]</span></td>
<td>durst <span style="color: #c0c0c0;" data-mce-mark="1">[dɜːst]</span></td>
<td>dared <span style="color: #c0c0c0;" data-mce-mark="1">[deəd]</span></td>
<td>сметь</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>40</td>
<td>deal <span style="color: #c0c0c0;" data-mce-mark="1">[diːl]</span></td>
<td>dealt <span style="color: #c0c0c0;" data-mce-mark="1">[delt]</span></td>
<td>dealt <span style="color: #c0c0c0;" data-mce-mark="1">[delt]</span></td>
<td>иметь дело, торговать, рассматривать вопрос</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>41</td>
<td>dig <span style="color: #c0c0c0;" data-mce-mark="1">[dɪɡ]</span></td>
<td>dug <span style="color: #c0c0c0;" data-mce-mark="1">[dʌɡ]</span></td>
<td>dug <span style="color: #c0c0c0;" data-mce-mark="1">[dʌɡ]</span></td>
<td>копать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>42</td>
<td>dive <span style="color: #c0c0c0;" data-mce-mark="1">[daɪv]</span></td>
<td>dove <span style="color: #c0c0c0;" data-mce-mark="1">[dʌv]</span></td>
<td>dived <span style="color: #c0c0c0;" data-mce-mark="1">[daɪvd]</span></td>
<td>нырять</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>43</td>
<td>do/does <span style="color: #c0c0c0;" data-mce-mark="1">[dʌz]</span></td>
<td>did <span style="color: #c0c0c0;" data-mce-mark="1">[dɪd]</span></td>
<td>done <span style="color: #c0c0c0;" data-mce-mark="1">[dʌn]</span></td>
<td>делать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>44</td>
<td>draw <span style="color: #c0c0c0;" data-mce-mark="1">[drɔː]</span></td>
<td>drew <span style="color: #c0c0c0;" data-mce-mark="1">[druː]</span></td>
<td>drawn <span style="color: #c0c0c0;" data-mce-mark="1">[drɔːn]</span></td>
<td>тащить, чертить</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>45</td>
<td>dream <span style="color: #c0c0c0;" data-mce-mark="1">[driːm]</span></td>
<td>dreamt <span style="color: #c0c0c0;" data-mce-mark="1">[dremt]</span></td>
<td>dreamt <span style="color: #c0c0c0;" data-mce-mark="1">[dremt]</span></td>
<td>видеть сны, мечтать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>46</td>
<td>drink <span style="color: #c0c0c0;" data-mce-mark="1">[drɪŋk]</span></td>
<td>drank <span style="color: #c0c0c0;" data-mce-mark="1">[dræŋk]</span></td>
<td>drunk <span style="color: #c0c0c0;" data-mce-mark="1">[drʌŋk]</span></td>
<td>пить, выпивать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>47</td>
<td>drive <span style="color: #c0c0c0;" data-mce-mark="1">[draɪv]</span></td>
<td>drove <span style="color: #c0c0c0;" data-mce-mark="1">[drəʊv]</span></td>
<td>driven <span style="color: #c0c0c0;" data-mce-mark="1">[ˈdrɪvn̩]</span></td>
<td>ехать, везти, водить, гнать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>48</td>
<td>dwell <span style="color: #c0c0c0;" data-mce-mark="1">[dwel]</span></td>
<td>dwelt <span style="color: #c0c0c0;" data-mce-mark="1">[dwelt]</span></td>
<td>dwelt <span style="color: #c0c0c0;" data-mce-mark="1">[dwelt]</span></td>
<td>обитать, пребывать, задерживаться на чем-либо</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>49</td>
<td>eat <span style="color: #c0c0c0;" data-mce-mark="1">[iːt]</span></td>
<td>ate <span style="color: #c0c0c0;" data-mce-mark="1">[et]</span></td>
<td>eaten <span style="color: #c0c0c0;" data-mce-mark="1">[ˈiːtn̩]</span></td>
<td>есть, принимать пищу, кушать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>50</td>
<td>fall <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːl]</span></td>
<td>fell <span style="color: #c0c0c0;" data-mce-mark="1">[fel]</span></td>
<td>fallen <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːlən]</span></td>
<td>падать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>51</td>
<td>feed <span style="color: #c0c0c0;" data-mce-mark="1">[fiːd]</span></td>
<td>fed <span style="color: #c0c0c0;" data-mce-mark="1">[fed]</span></td>
<td>fed <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">fed</span>]</span></td>
<td>кормить(ся)</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>52</td>
<td>feel <span style="color: #c0c0c0;" data-mce-mark="1">[fiːl]</span></td>
<td>felt <span style="color: #c0c0c0;" data-mce-mark="1">[felt]</span></td>
<td>felt <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">felt</span>]</span></td>
<td>чувствовать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>53</td>
<td>fight <span style="color: #c0c0c0;" data-mce-mark="1">[faɪt]</span></td>
<td>fought <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːt ]</span></td>
<td>fought <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːt ]</span></td>
<td>бороться, сражаться</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>54</td>
<td>find <span style="color: #c0c0c0;" data-mce-mark="1">[faɪnd]</span></td>
<td>found <span style="color: #c0c0c0;" data-mce-mark="1">[faʊnd]</span></td>
<td>found <span style="color: #c0c0c0;" data-mce-mark="1">[faʊnd]</span></td>
<td>находить</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>55</td>
<td>fit <span style="color: #c0c0c0;" data-mce-mark="1">[fɪt]</span></td>
<td>fit <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">fɪt</span>]</span></td>
<td>fit <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">fɪt</span>]</span></td>
<td>подходить, годиться</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>56</td>
<td>flee <span style="color: #c0c0c0;" data-mce-mark="1">[fliː]</span></td>
<td>fled <span style="color: #c0c0c0;" data-mce-mark="1">[fled]</span></td>
<td>fled <span style="color: #c0c0c0;" data-mce-mark="1">[fled]</span></td>
<td>бежать, спасаться бегством</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>57</td>
<td>fling <span style="color: #c0c0c0;" data-mce-mark="1">[flɪŋ]</span></td>
<td>flung <span style="color: #c0c0c0;" data-mce-mark="1">[flʌŋ]</span></td>
<td>flung <span style="color: #c0c0c0;" data-mce-mark="1">[flʌŋ]</span></td>
<td>кидать, бросать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>58</td>
<td>fly <span style="color: #c0c0c0;" data-mce-mark="1">[flaɪ]</span></td>
<td>flew <span style="color: #c0c0c0;" data-mce-mark="1">[fluː]</span></td>
<td>flown <span style="color: #c0c0c0;" data-mce-mark="1">[fləʊn]</span></td>
<td>летать, пролетать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>59</td>
<td>forbid <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈbɪd]</span></td>
<td>forbade <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈbæd]</span></td>
<td>forbidden <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈbɪdn̩]</span></td>
<td>запрещать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>60</td>
<td>forecast <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːkɑːst]</span></td>
<td>forecast;&nbsp;forecasted <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːkɑːstɪd]</span></td>
<td>forecast;&nbsp;forecasted <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfɔːkɑːstɪd]</span></td>
<td>предвидеть,&nbsp;предсказывать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>61</td>
<td>forget <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡet]</span></td>
<td>forgot <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡɒt]</span></td>
<td>forgotten <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡɒtn̩]</span></td>
<td>забывать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>62</td>
<td>forego <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈɡəʊ]</span></td>
<td>forewent <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈwent]</span></td>
<td>foregone <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈɡɒn]</span></td>
<td>отказываться, воздерживаться</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>63</td>
<td>foretell <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈtel]</span></td>
<td>foretold <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈtəʊld]</span></td>
<td>foretold <span style="color: #c0c0c0;" data-mce-mark="1">[fɔːˈtəʊld]</span></td>
<td>предсказывать, прогнозировать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>64</td>
<td>forgive <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡɪv]</span></td>
<td>forgave <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡeɪv]</span></td>
<td>forgiven <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈɡɪvn̩]</span></td>
<td>прощать,</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>65</td>
<td>forsake <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈseɪk]</span></td>
<td>forsook <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈsʊk]</span></td>
<td>forsaken <span style="color: #c0c0c0;" data-mce-mark="1">[fəˈseɪkən]</span></td>
<td>бросать, отказываться</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>66</td>
<td>freeze <span style="color: #c0c0c0;" data-mce-mark="1">[friːz]</span></td>
<td>froze <span style="color: #c0c0c0;" data-mce-mark="1">[frəʊz]</span></td>
<td>frozen <span style="color: #c0c0c0;" data-mce-mark="1">[ˈfrəʊzən]</span></td>
<td>замерзать, замораживать</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>67</td>
<td>get <span style="color: #c0c0c0;" data-mce-mark="1">[ˈɡet]</span></td>
<td>got <span style="color: #c0c0c0;" data-mce-mark="1">[ˈɡɒt]</span></td>
<td>got <span style="color: #c0c0c0;" data-mce-mark="1">[ˈɡɒt]</span></td>
<td>получать, становиться</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>68</td>
<td>gild <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɪld]</span></td>
<td>gilt <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɪlt]</span>;&nbsp;gilded <span style="color: #c0c0c0;" data-mce-mark="1">[ˈɡɪldɪd]</span></td>
<td>gilt <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɪlt]</span>;&nbsp;gilded <span style="color: #c0c0c0;" data-mce-mark="1">[ˈɡɪldɪd]</span></td>
<td>позолотить</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>69</td>
<td>give <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɪv]</span></td>
<td>gave <span style="color: #c0c0c0;" data-mce-mark="1">[ɡeɪv]</span></td>
<td>given <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɪvn̩]</span></td>
<td>давать</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>70</td>
<td>go/goes <span style="color: #c0c0c0;" data-mce-mark="1">[ɡəʊz]</span></td>
<td>went <span style="color: #c0c0c0;" data-mce-mark="1">[ˈwent]</span></td>
<td>gone <span style="color: #c0c0c0;" data-mce-mark="1">[ɡɒn]</span></td>
<td>идти, ехать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>71</td>
<td>grind <span style="color: #c0c0c0;" data-mce-mark="1">[ɡraɪnd]</span></td>
<td>ground <span style="color: #c0c0c0;" data-mce-mark="1">[ɡraʊnd]</span></td>
<td>ground <span style="color: #c0c0c0;" data-mce-mark="1">[ɡraʊnd]</span></td>
<td>точить, молоть</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>72</td>
<td>grow <span style="color: #c0c0c0;" data-mce-mark="1">[ɡrəʊ]</span></td>
<td>grew <span style="color: #c0c0c0;" data-mce-mark="1">[ɡruː]</span></td>
<td>grown <span style="color: #c0c0c0;" data-mce-mark="1">[ɡrəʊn]</span></td>
<td>расти, выращивать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>73</td>
<td>hang <span style="color: #c0c0c0;" data-mce-mark="1">[hæŋ]</span></td>
<td>hung <span style="color: #c0c0c0;" data-mce-mark="1">[hʌŋ]</span>; hanged <span style="color: #c0c0c0;" data-mce-mark="1">[hæŋd]</span></td>
<td>hung <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">hʌŋ</span>]</span>; hanged <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">hæŋd</span>]</span></td>
<td>висеть, вешать</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>74</td>
<td>have <span style="color: #c0c0c0;" data-mce-mark="1">[hæv]</span></td>
<td>had <span style="color: #c0c0c0;" data-mce-mark="1">[hæd]</span></td>
<td>had <span style="color: #c0c0c0;" data-mce-mark="1">[hæd]</span></td>
<td>иметь, обладать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>75</td>
<td>hew <span style="color: #c0c0c0;" data-mce-mark="1">[hjuː]</span></td>
<td>hewed <span style="color: #c0c0c0;" data-mce-mark="1">[hjuːd]</span></td>
<td>hewed <span style="color: #c0c0c0;" data-mce-mark="1">[hjuːd]</span>; hewn <span style="color: #c0c0c0;" data-mce-mark="1">[hjuːn]</span></td>
<td>рубить, тесать</td>
</tr>
<tr class="let2 pop" style="display: table-row;">
<td>76</td>
<td>hear <span style="color: #c0c0c0;" data-mce-mark="1">[hɪə]</span></td>
<td>heard <span style="color: #c0c0c0;" data-mce-mark="1">[hɜːd]</span></td>
<td>heard <span style="color: #c0c0c0;" data-mce-mark="1">[hɜːd]</span></td>
<td>слышать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>77</td>
<td>hide <span style="color: #c0c0c0;" data-mce-mark="1">[haɪd]</span></td>
<td>hid <span style="color: #c0c0c0;" data-mce-mark="1">[hɪd]</span></td>
<td>hidden <span style="color: #c0c0c0;" data-mce-mark="1">[ˈhɪdn̩]</span></td>
<td>прятать, прятаться</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>78</td>
<td>hit <span style="color: #c0c0c0;" data-mce-mark="1">[hɪt]</span></td>
<td>hit <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">hɪt</span>]</span></td>
<td>hit <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1"><span style="color: #c0c0c0;" data-mce-mark="1">hɪt</span>]</span></td>
<td>ударять, поражать</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>79</td>
<td>hold <span style="color: #c0c0c0;" data-mce-mark="1">[həʊld]</span></td>
<td>held <span style="color: #c0c0c0;" data-mce-mark="1">[held]</span></td>
<td>held <span style="color: #c0c0c0;" data-mce-mark="1">[held]</span></td>
<td>держать, поддерживать (владеть)</td>
</tr>
<tr class="let2" style="display: table-row;">
<td>80</td>
<td>hurt <span style="color: #c0c0c0;" data-mce-mark="1">[hɜːt]</span></td>
<td>hurt <span style="color: #c0c0c0;" data-mce-mark="1">[hɜːt]</span></td>
<td>hurt <span style="color: #c0c0c0;" data-mce-mark="1">[hɜːt]</span></td>
<td>повредить, причинять боль, ранить</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>81</td>
<td>keep <span style="color: #c0c0c0;" data-mce-mark="1">[kiːp</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>kept <span style="color: #c0c0c0;" data-mce-mark="1">[kept </span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>kept <span style="color: #c0c0c0;" data-mce-mark="1">[kept </span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>держать, хранить</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>82</td>
<td>kneel <span style="color: #c0c0c0;" data-mce-mark="1">[niːl</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>knelt <span style="color: #c0c0c0;" data-mce-mark="1">[nelt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>;&nbsp;kneeled <span style="color: #c0c0c0;" data-mce-mark="1">[niːld</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>knelt <span style="color: #c0c0c0;" data-mce-mark="1">[nelt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>;&nbsp;kneeled <span style="color: #c0c0c0;" data-mce-mark="1">[niːld</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>становиться на колени</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>83</td>
<td>knit <span style="color: #c0c0c0;" data-mce-mark="1">[nɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>knit <span style="color: #c0c0c0;" data-mce-mark="1">[nɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; knitted <span style="color: #c0c0c0;" data-mce-mark="1">[ˈnɪtɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>knit <span style="color: #c0c0c0;" data-mce-mark="1">[nɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; knitted <span style="color: #c0c0c0;" data-mce-mark="1">[ˈnɪtɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>вязать</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>84</td>
<td>know <span style="color: #c0c0c0;" data-mce-mark="1">[nəʊ</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>knew <span style="color: #c0c0c0;" data-mce-mark="1">[njuː</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>known <span style="color: #c0c0c0;" data-mce-mark="1">[nəʊn</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>знать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>85</td>
<td>lay <span style="color: #c0c0c0;" data-mce-mark="1">[leɪ</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>laid <span style="color: #c0c0c0;" data-mce-mark="1">[leɪd </span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>laid <span style="color: #c0c0c0;" data-mce-mark="1">[leɪd </span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>класть</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>86</td>
<td>lead <span style="color: #c0c0c0;" data-mce-mark="1">[liːd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>led <span style="color: #c0c0c0;" data-mce-mark="1">[led</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>led <span style="color: #c0c0c0;" data-mce-mark="1">[led</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>вести, сопровождать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>87</td>
<td>lean <span style="color: #c0c0c0;" data-mce-mark="1">[liːn</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>leant <span style="color: #c0c0c0;" data-mce-mark="1">[lent</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; leaned <span style="color: #c0c0c0;" data-mce-mark="1">[liːnd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>leant <span style="color: #c0c0c0;" data-mce-mark="1">[lent</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; leaned <span style="color: #c0c0c0;" data-mce-mark="1">[liːnd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>опираться, прислоняться</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>88</td>
<td>leap <span style="color: #c0c0c0;" data-mce-mark="1">[liːp</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>leapt <span style="color: #c0c0c0;" data-mce-mark="1">[lept</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; leaped <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">liːpt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>leapt <span style="color: #c0c0c0;" data-mce-mark="1">[lept</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; leaped <span style="color: #c0c0c0;" data-mce-mark="1">[liːpt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>прыгать</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>89</td>
<td>learn <span style="color: #c0c0c0;" data-mce-mark="1">[lɜːn</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>learnt <span style="color: #c0c0c0;" data-mce-mark="1">[lɜːnt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; learned <span style="color: #c0c0c0;" data-mce-mark="1">[lɜːnd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>learnt <span style="color: #c0c0c0;" data-mce-mark="1">[lɜːnt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; learned <span style="color: #c0c0c0;" data-mce-mark="1">[lɜːnd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>учиться, узнавать</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>90</td>
<td>leave <span style="color: #c0c0c0;" data-mce-mark="1">[liːv</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>left <span style="color: #c0c0c0;" data-mce-mark="1">[left</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>left <span style="color: #c0c0c0;" data-mce-mark="1">[left</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>оставлять, уезжать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>91</td>
<td>lend <span style="color: #c0c0c0;" data-mce-mark="1">[lend</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lent <span style="color: #c0c0c0;" data-mce-mark="1">[lent</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lent <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">lent</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>одалживать, давать взаймы</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>92</td>
<td>let <span style="color: #c0c0c0;" data-mce-mark="1">[let</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>let <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">let</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>let <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">let</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>позволять, сдавать в наём</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>93</td>
<td>lie <span style="color: #c0c0c0;" data-mce-mark="1">[laɪ</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lay <span style="color: #c0c0c0;" data-mce-mark="1">[leɪ</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lain <span style="color: #c0c0c0;" data-mce-mark="1">[leɪn</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>лежать</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>94</td>
<td>light <span style="color: #c0c0c0;" data-mce-mark="1">[laɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lit <span style="color: #c0c0c0;" data-mce-mark="1">[lɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; lighted <span style="color: #c0c0c0;" data-mce-mark="1">[ˈlaɪtɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lit <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">lɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span>; lighted <span style="color: #c0c0c0;" data-mce-mark="1">[</span><span style="color: #c0c0c0;" data-mce-mark="1">ˈlaɪtɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>зажигать, освещать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>95</td>
<td>lose <span style="color: #c0c0c0;" data-mce-mark="1">[luːz</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lost <span style="color: #c0c0c0;" data-mce-mark="1">[lɒst</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>lost <span style="color: #c0c0c0;" data-mce-mark="1">[lɒst</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>терять</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>96</td>
<td>make <span style="color: #c0c0c0;" data-mce-mark="1">[ˈmeɪk</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>made <span style="color: #c0c0c0;" data-mce-mark="1">[ˈmeɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>made <span style="color: #c0c0c0;" data-mce-mark="1">[ˈmeɪd</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>делать, заставлять</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>97</td>
<td>may <span style="color: #c0c0c0;" data-mce-mark="1">[meɪ</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>might <span style="color: #c0c0c0;" data-mce-mark="1">[maɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>might <span style="color: #c0c0c0;" data-mce-mark="1">[maɪt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>мочь, иметь право</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>98</td>
<td>mean <span style="color: #c0c0c0;" data-mce-mark="1">[miːn</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>meant <span style="color: #c0c0c0;" data-mce-mark="1">[ment</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>meant <span style="color: #c0c0c0;" data-mce-mark="1">[ment</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>значить, подразумевать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>99</td>
<td>meet <span style="color: #c0c0c0;" data-mce-mark="1">[miːt</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>met <span style="color: #c0c0c0;" data-mce-mark="1">[met</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>met <span style="color: #c0c0c0;" data-mce-mark="1">[met</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>встречать, знакомиться</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>100</td>
<td>mishear <span style="color: #c0c0c0;" data-mce-mark="1">[ˌmɪsˈhɪə</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>misheard <span style="color: #c0c0c0;" data-mce-mark="1">[ˌmɪsˈhɪə</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>misheard <span style="color: #c0c0c0;" data-mce-mark="1">[ˌmɪsˈhɪə</span><span style="color: #c0c0c0;" data-mce-mark="1">]</span></td>
<td>ослышаться</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>101</td>
<td>mislay</td>
<td>mislaid</td>
<td>mislaid</td>
<td>класть не на место</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>102</td>
<td>mistake</td>
<td>mistook</td>
<td>mistaken</td>
<td>ошибаться, заблуждаться</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>103</td>
<td>mow</td>
<td>mowed</td>
<td>mown</td>
<td>косить</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>104</td>
<td>overtake</td>
<td>overtook</td>
<td>overtaken</td>
<td>догнать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>105</td>
<td>pay</td>
<td>paid</td>
<td>paid</td>
<td>платить</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>106</td>
<td>prove</td>
<td>proved</td>
<td>proved; proven</td>
<td>доказывать, удостоверять</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>107</td>
<td>put</td>
<td>put</td>
<td>put</td>
<td>класть</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>108</td>
<td>quit</td>
<td>quit; quitted</td>
<td>quit; quitted</td>
<td>оставлять, покидать</td>
</tr>
<tr class="let3 pop" style="display: table-row;">
<td>109</td>
<td>read</td>
<td>read; red</td>
<td>read; red</td>
<td>читать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>110</td>
<td>rebuild</td>
<td>rebuilt</td>
<td>rebuilt</td>
<td>перестраивать, восстанавливать</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>111</td>
<td>rid</td>
<td>rid; ridded</td>
<td>rid; ridded</td>
<td>освобождать, избавлять</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>112</td>
<td>ride</td>
<td>rode</td>
<td>ridden</td>
<td>ехать верхом</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>113</td>
<td>ring</td>
<td>rang</td>
<td>rung</td>
<td>звонить, звенеть</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>114</td>
<td>rise</td>
<td>rose</td>
<td>risen</td>
<td>подниматься, восходить</td>
</tr>
<tr class="let3" style="display: table-row;">
<td>115</td>
<td>run</td>
<td>ran</td>
<td>run</td>
<td>бежать, течь</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>116</td>
<td>saw</td>
<td>sawed</td>
<td>sawn; sawed</td>
<td>пилить</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>117</td>
<td>say</td>
<td>said</td>
<td>said</td>
<td>говорить, сказать</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>118</td>
<td>see</td>
<td>saw</td>
<td>seen</td>
<td>видеть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>119</td>
<td>seek</td>
<td>sought</td>
<td>sought</td>
<td>искать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>120</td>
<td>sell</td>
<td>sold</td>
<td>sold</td>
<td>продавать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>121</td>
<td>send</td>
<td>sent</td>
<td>sent</td>
<td>посылать, отправлять</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>122</td>
<td>set</td>
<td>set</td>
<td>set</td>
<td>помещать, ставить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>123</td>
<td>sew</td>
<td>sewed</td>
<td>sewed; sewn</td>
<td>шить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>124</td>
<td>shake</td>
<td>shook</td>
<td>shaken</td>
<td>трясти</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>125</td>
<td>shall</td>
<td>should</td>
<td>should</td>
<td>быть должным</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>126</td>
<td>shave</td>
<td>shaved</td>
<td>shaved</td>
<td>брить(ся)</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>127</td>
<td>shear</td>
<td>sheared</td>
<td>shorn</td>
<td>стричь, резать; лишать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>128</td>
<td>shed</td>
<td>shed</td>
<td>shed</td>
<td>сбрасывать, проливать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>129</td>
<td>shine</td>
<td>shone; shined</td>
<td>shone; shined</td>
<td>сиять, светить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>130</td>
<td>shoe</td>
<td>shod</td>
<td>shod</td>
<td>обувать, подковывать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>131</td>
<td>shoot</td>
<td>shot</td>
<td>shot</td>
<td>стрелять</td>
</tr>
<tr class="let4 pop" style="display: table-row;">
<td>132</td>
<td>show</td>
<td>showed</td>
<td>shown; showed</td>
<td>показывать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>133</td>
<td>shrink</td>
<td>shrank; shrunk</td>
<td>shrunk</td>
<td>сокращаться, сжиматься, отскочить, отпрянуть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>134</td>
<td>shut</td>
<td>shut</td>
<td>shut</td>
<td>закрывать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>135</td>
<td>sing</td>
<td>sang</td>
<td>sung</td>
<td>петь</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>136</td>
<td>sink</td>
<td>sank</td>
<td>sunk</td>
<td>опускаться, погружаться, тонуть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>137</td>
<td>sit</td>
<td>sat</td>
<td>sat</td>
<td>сидеть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>138</td>
<td>slay</td>
<td>slew</td>
<td>slain</td>
<td>убивать, уничтожать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>139</td>
<td>sleep</td>
<td>slept</td>
<td>slept</td>
<td>спать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>140</td>
<td>slide</td>
<td>slid</td>
<td>slid</td>
<td>скользить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>141</td>
<td>sling</td>
<td>slung</td>
<td>slung</td>
<td>швырять, швырнуть, вешать через плечо, подвешивать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>142</td>
<td>slit</td>
<td>slit</td>
<td>slit</td>
<td>резать в длину, вдоль</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>143</td>
<td>smell</td>
<td>smelt; smelled</td>
<td>smelt; smelled</td>
<td>пахнуть, нюхать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>144</td>
<td>sow</td>
<td>sowed</td>
<td>sowed; sown</td>
<td>сеять</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>145</td>
<td>speak</td>
<td>spoke</td>
<td>spoken</td>
<td>говорить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>146</td>
<td>speed</td>
<td>sped; speeded</td>
<td>sped; speeded</td>
<td>спешить, ускорять</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>147</td>
<td>spell</td>
<td>spelt; spelled</td>
<td>spelt; spelled</td>
<td>писать, произносить слово по буквам</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>148</td>
<td>spend</td>
<td>spent</td>
<td>spent</td>
<td>тратить, истощать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>149</td>
<td>spill</td>
<td>spilt</td>
<td>spilt</td>
<td>проливать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>150</td>
<td>spin</td>
<td>spun</td>
<td>spun</td>
<td>прясть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>151</td>
<td>spit</td>
<td>spat</td>
<td>spat</td>
<td>плевать, насаживать, натыкать, про-</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>152</td>
<td>split</td>
<td>split</td>
<td>split</td>
<td>раскалывать, расщеплять</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>153</td>
<td>spoil</td>
<td>spoilt; spoiled</td>
<td>spoilt; spoiled</td>
<td>портить, баловать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>154</td>
<td>spread</td>
<td>spread</td>
<td>spread</td>
<td>распространяться</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>155</td>
<td>spring</td>
<td>sprang</td>
<td>sprung</td>
<td>прыгать, вскочить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>156</td>
<td>stand</td>
<td>stood</td>
<td>stood</td>
<td>стоять</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>157</td>
<td>steal</td>
<td>stole</td>
<td>stolen</td>
<td>воровать, красть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>158</td>
<td>stick</td>
<td>stuck</td>
<td>stuck</td>
<td>втыкать, приклеивать(ся), липнуть</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>159</td>
<td>sting</td>
<td>stung</td>
<td>stung</td>
<td>жалить</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>160</td>
<td>stink</td>
<td>stank; stunk</td>
<td>stunk</td>
<td>вонять, отталкивать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>161</td>
<td>strew</td>
<td>strewed</td>
<td>strewn; strewed</td>
<td>усеять, разбрасывать, расстилать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>162</td>
<td>stride</td>
<td>strode</td>
<td>stridden</td>
<td>шагать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>163</td>
<td>strike</td>
<td>struck</td>
<td>struck</td>
<td>ударять, поражать, бастовать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>164</td>
<td>string</td>
<td>strung</td>
<td>strung</td>
<td>связывать, натягивать, нанизывать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>165</td>
<td>strive</td>
<td>strove</td>
<td>striven</td>
<td>стремиться, стараться</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>166</td>
<td>swear</td>
<td>swore</td>
<td>sworn</td>
<td>клясться, присягать, браниться</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>167</td>
<td>sweep</td>
<td>swept</td>
<td>swept</td>
<td>мести</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>168</td>
<td>swell</td>
<td>swelled</td>
<td>swollen; swelled</td>
<td>пухнуть, раздуваться, набухать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>169</td>
<td>swim</td>
<td>swam</td>
<td>swum</td>
<td>плавать</td>
</tr>
<tr class="let4" style="display: table-row;">
<td>170</td>
<td>swing</td>
<td>swung</td>
<td>swung</td>
<td>качать(ся), размахивать</td>
</tr>
<tr class="let5 pop" style="display: table-row;">
<td>171</td>
<td>take</td>
<td>took</td>
<td>taken</td>
<td>брать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>172</td>
<td>teach</td>
<td>taught</td>
<td>taught</td>
<td>обучать, учить</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>173</td>
<td>tear</td>
<td>tore</td>
<td>torn</td>
<td>рвать, раз-, с-, от-</td>
</tr>
<tr class="let5 pop" style="display: table-row;">
<td>174</td>
<td>tell</td>
<td>told</td>
<td>told</td>
<td>рассказывать, сообщать</td>
</tr>
<tr class="let5 pop" style="display: table-row;">
<td>175</td>
<td>think</td>
<td>thought</td>
<td>thought</td>
<td>думать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>176</td>
<td>throw</td>
<td>threw</td>
<td>thrown</td>
<td>кидать, бросать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>177</td>
<td>thrust</td>
<td>thrust</td>
<td>thrust</td>
<td>толкать, колоть, выгонять, сунуть</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>178</td>
<td>tread</td>
<td>trod</td>
<td>trod; trodden</td>
<td>ступать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>179</td>
<td>unbend</td>
<td>unbent</td>
<td>unbent</td>
<td>разгибаться</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>180</td>
<td>undergo</td>
<td>underwent</td>
<td>undergone</td>
<td>испытывать, переносить</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>181</td>
<td>understand</td>
<td>understood</td>
<td>understood</td>
<td>понимать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>182</td>
<td>undertake</td>
<td>undertook</td>
<td>undertaken</td>
<td>предпринимать, гарантировать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>183</td>
<td>upset</td>
<td>upset</td>
<td>upset</td>
<td>опрокидывать, обжимать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>184</td>
<td>wake</td>
<td>woke; waked</td>
<td>woken; waked</td>
<td>будить, просыпаться</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>185</td>
<td>wear</td>
<td>wore</td>
<td>worn</td>
<td>носить (одежду)</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>186</td>
<td>weave</td>
<td>wove; weaved</td>
<td>woven; weaved</td>
<td>ткать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>187</td>
<td>wed</td>
<td>wed; wedded</td>
<td>wed; wedded</td>
<td>венчать(ся), выдавать замуж</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>188</td>
<td>weep</td>
<td>wept</td>
<td>wept</td>
<td>плакать</td>
</tr>
<tr class="let5 pop" style="display: table-row;">
<td>189</td>
<td>will</td>
<td>would</td>
<td>would</td>
<td>хотеть быть</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>190</td>
<td>wet</td>
<td>wet; wetted</td>
<td>wet; wetted</td>
<td>мочить, вы-, про-</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>191</td>
<td>win</td>
<td>won</td>
<td>won</td>
<td>выигрывать, получать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>192</td>
<td>wind</td>
<td>wound</td>
<td>wound</td>
<td>заводить (механизм), виться</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>193</td>
<td>withdraw</td>
<td>withdrew</td>
<td>withdrawn</td>
<td>брать назад, отнимать</td>
</tr>
<tr class="let5" style="display: table-row;">
<td>194</td>
<td>wring</td>
<td>wrung</td>
<td>wrung</td>
<td>жать, выжимать, скручивать</td>
</tr>
<tr class="let5 pop" style="display: table-row;">
<td>195</td>
<td>write</td>
<td>wrote</td>
<td>written</td>
<td>писать</td>
</tr>
"""

words = list()

for find in re.findall('<td.*?>(.+?)</td>', content):
    word = find.split('<')[0].split('&')[0]
    words.append(word)

dictionary = dict()

for word in range(0, len(words), 5):
    dictionary[words[word]] = {
        'infinitive': words[word+1],
        'past_simple': words[word+2],
        'perfect': words[word+3],
        'russian_translate': words[word+4]
    }


with open('words.json', 'w') as f:
    json.dump(dictionary, f)

