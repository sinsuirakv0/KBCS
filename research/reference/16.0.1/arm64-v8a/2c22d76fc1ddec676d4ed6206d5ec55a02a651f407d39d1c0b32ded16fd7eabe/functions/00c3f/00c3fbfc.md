# 00c3fbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c3fbfc",
  "name": "FUN_00c3fbfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc",
  "source_text_sha256": "53332f93d95124f80dfa4284d962799d75d0f5cd932936d34dcac8591946d1dc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 583 bytes

~~~c

byte FUN_00c3fbfc(long param_1)

{
  ushort uVar1;
  byte bVar2;
  long *plVar3;
  
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    plVar3 = *(long **)(param_1 + 0x18);
    *(undefined1 *)(param_1 + 0x20) = 1;
    uVar1 = *(ushort *)((long)plVar3 + 9) >> 10 & 3;
                    /* try { // try from 00c3fc34 to 00d3fcbb has its CatchHandler @ 00c3fda0 */
    if (uVar1 == 2) {
      bVar2 = (**(code **)(*plVar3 + 0x10))(plVar3);
    }
    else {
      bVar2 = uVar1 == 0;
    }
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  else {
    bVar2 = 0;
  }
  return bVar2 & 1;
}

~~~
