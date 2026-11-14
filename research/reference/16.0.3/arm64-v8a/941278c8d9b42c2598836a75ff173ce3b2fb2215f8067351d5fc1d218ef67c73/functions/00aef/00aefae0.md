# 00aefae0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aefae0",
  "name": "FUN_00aefae0",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97611cfd4de4bfbd71aadf9127be242e068296ee6f941e8ff2a1087da6b4558e",
  "source_text_sha256": "97611cfd4de4bfbd71aadf9127be242e068296ee6f941e8ff2a1087da6b4558e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)
- [008ba854](../008ba/008ba854.md)
- [008bc514](../008bc/008bc514.md)

## 疑似コード / UTF-8 472 bytes

~~~c

void FUN_00aefae0(long param_1,undefined8 param_2,int *param_3)

{
  undefined8 uVar1;
  long lVar2;
  
  if (*param_3 == 3) {
    lVar2 = *(long *)(param_1 + 8);
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    uVar1 = FUN_008bc514(lVar2 + 0x2f08);
    FUN_008ba854(uVar1,2);
    FUN_008bc514(lVar2 + 0x2f08);
    FUN_008ba17c();
    return;
  }
  if (*param_3 == 0) {
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,10,0);
    return;
  }
  return;
}

~~~
