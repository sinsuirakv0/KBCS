# 00aefbc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aefbc4",
  "name": "FUN_00aefbc4",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07b5c2edadc208e9dac81e8de1b41bde6e6af6638287f8d1d14702a687f4108e",
  "source_text_sha256": "07b5c2edadc208e9dac81e8de1b41bde6e6af6638287f8d1d14702a687f4108e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)

## 疑似コード / UTF-8 276 bytes

~~~c

void FUN_00aefbc4(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    uVar2 = *param_2;
    uVar1 = FUN_0047b054();
    FUN_0047d134(uVar1,0xb,0);
    FUN_008ba17c(uVar2);
    return;
  }
  return;
}

~~~
