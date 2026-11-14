# 007feeac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007feeac",
  "name": "FUN_007feeac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df34f5d91230c4c6444ed437c0f05c0eca73bdf2fffaacf4e2b7e28682184053",
  "source_text_sha256": "df34f5d91230c4c6444ed437c0f05c0eca73bdf2fffaacf4e2b7e28682184053"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)

## 疑似コード / UTF-8 470 bytes

~~~c

void FUN_007feeac(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
                    /* try { // try from 007feec0 to 008feed3 has its CatchHandler @ 007ff05c */
    uVar2 = *param_2;
    uVar1 = FUN_0047b054();
                    /* try { // try from 007feed4 to 008feee3 has its CatchHandler @ 007ff048 */
    FUN_0047d134(uVar1,0xb,0);
    FUN_008ba17c(uVar2);
    return;
  }
  return;
}

~~~
