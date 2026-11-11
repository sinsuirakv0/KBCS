# 009ffeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009ffeec",
  "name": "FUN_009ffeec",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51d1bffb301ca667925f956e35ebfd3c28a2d25676102514ff6dd723a0a24cbc",
  "source_text_sha256": "51d1bffb301ca667925f956e35ebfd3c28a2d25676102514ff6dd723a0a24cbc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 752 bytes

~~~c

void FUN_009ffeec(long param_1,undefined8 *param_2)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  plVar1 = *(long **)(param_1 + 0x30);
  *param_2 = &PTR_FUN_00c8a810;
  if (plVar1 == (long *)0x0) {
    param_2[6] = 0;
  }
  else if (plVar1 == (long *)(param_1 + 0x10)) {
    param_2[6] = param_2 + 2;
    (**(code **)(**(long **)(param_1 + 0x30) + 0x18))();
  }
  else {
    uVar2 = (**(code **)(*plVar1 + 0x10))();
    param_2[6] = uVar2;
  }
  uVar3 = *(undefined8 *)(param_1 + 0x48);
  uVar2 = *(undefined8 *)(param_1 + 0x40);
                    /* try { // try from 009fff58 to 00afff77 has its CatchHandler @ 00a00f94 */
  param_2[10] = *(undefined8 *)(param_1 + 0x50);
  param_2[9] = uVar3;
  param_2[8] = uVar2;
  return;
}

~~~
