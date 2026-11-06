# 00bbb5ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbb5ac.md)

## 関数情報

~~~json
{
  "address": "00bbb5ac",
  "name": "__dynamic_cast",
  "size": 524,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b220ebd7a75eac874a02dfa03d7456f1d01990d1b061199c0e2bbfb3edfadcf",
  "source_text_sha256": "6b220ebd7a75eac874a02dfa03d7456f1d01990d1b061199c0e2bbfb3edfadcf"
}
~~~
## 呼び出し元

- [00bdb7c0](../00bdb/00bdb7c0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 3228 bytes

~~~c

long __dynamic_cast(long *param_1,undefined8 param_2,long *param_3,long param_4)

{
  long *plVar1;
  bool bVar2;
  long lVar3;
  long lVar4;
  long *local_98;
  long *plStack_90;
  long *local_88;
  long lStack_80;
  long local_78;
  long lStack_70;
  undefined8 local_68;
  int iStack_60;
  int iStack_5c;
  int local_58;
  undefined4 uStack_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined8 local_48;
  
                    /* try { // try from 00bbb5c8 to 00cbb5cf has its CatchHandler @ 00bbb8e8 */
  lVar3 = *(long *)(*param_1 + -0x10);
  plVar1 = *(long **)(*param_1 + -8);
  lVar4 = (long)param_1 + lVar3;
  lStack_80 = param_4;
  if (plVar1[1] == param_3[1]) {
    if (param_4 < 0) {
      if (param_4 == -2) {
        return 0;
      }
      local_50 = 1;
      local_58 = 0;
      uStack_54 = 0;
      local_48 = 0;
      lStack_70 = 0;
      local_78 = 0;
      iStack_60 = 0;
      iStack_5c = 0;
      local_68 = 0;
      local_4c = 0x1000000;
      local_98 = param_3;
      plStack_90 = param_1;
      local_88 = (long *)param_2;
      (**(code **)(*param_3 + 0x28))(param_3,&local_98,lVar4,lVar4,1,0);
      bVar2 = (int)local_68 == 1;
    }
    else {
      bVar2 = param_4 + lVar3 == 0;
    }
    if (!bVar2) {
      lVar4 = 0;
    }
  }
  else {
    if ((-1 < param_4) && (lVar3 = (long)param_1 - param_4, lVar4 <= lVar3)) {
                    /* try { // try from 00bbb604 to 00cbb60f has its CatchHandler @ 00bbb7ec */
                    /* try { // try from 00bbb610 to 00cbb61f has its CatchHandler @ 00bbb7d8 */
      local_58 = 0;
      uStack_54 = 0;
      iStack_60 = 0;
      iStack_5c = 0;
                    /* try { // try from 00bbb620 to 00cbb633 has its CatchHandler @ 00bbb7c0 */
      local_68 = 0;
      lStack_70 = 0;
      local_78 = 0;
      local_50 = 1;
      local_4c = 0x1000000;
      local_48 = 0;
      local_98 = plVar1;
      plStack_90 = (long *)lVar3;
      local_88 = param_3;
      (**(code **)(*plVar1 + 0x28))(plVar1,&local_98,lVar4,lVar4,1,0);
      if ((int)local_68 != 0) {
        return lVar3;
      }
    }
    local_48 = 0;
    local_50 = 0;
    local_4c = 0x1000000;
    local_58 = 0;
    uStack_54 = 0;
    lStack_70 = 0;
    local_78 = 0;
    iStack_60 = 0;
    iStack_5c = 0;
    local_68 = 0;
    local_98 = param_3;
    plStack_90 = param_1;
    local_88 = (long *)param_2;
    lStack_80 = param_4;
    (**(code **)(*plVar1 + 0x30))(plVar1,&local_98,lVar4,1,0);
    if (iStack_5c == 1) {
                    /* try { // try from 00bbb6f8 to 00cbb703 has its CatchHandler @ 00bbb8e8 */
                    /* try { // try from 00bbb704 to 00cbb92f has its CatchHandler @ 00bbaf68 */
      if (((int)local_68 == 1) ||
         (((lVar4 = 0, local_58 == 0 && (local_68._4_4_ == 1)) && (iStack_60 == 1)))) {
        lVar4 = local_78;
      }
    }
    else {
      lVar4 = 0;
                    /* try { // try from 00bbb6c8 to 00cbb6d3 has its CatchHandler @ 00bbb8ec */
                    /* try { // try from 00bbb6d4 to 00cbb6e3 has its CatchHandler @ 00bbb8f0 */
      if ((iStack_5c == 0) &&
         (lVar4 = lStack_70, (iStack_60 != 1 || local_68._4_4_ != 1) || local_58 != 1)) {
        lVar4 = 0;
      }
    }
  }
  return lVar4;
}

~~~
