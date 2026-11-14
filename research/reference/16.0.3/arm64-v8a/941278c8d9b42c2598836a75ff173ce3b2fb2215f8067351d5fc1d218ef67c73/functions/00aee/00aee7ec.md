# 00aee7ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aee7ec",
  "name": "FUN_00aee7ec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad5012715cfd541ece8a22f9f8d325afe0b02791c86941cfd8ccced96195b6b1",
  "source_text_sha256": "ad5012715cfd541ece8a22f9f8d325afe0b02791c86941cfd8ccced96195b6b1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_00aee7ec(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00aee7f8 to 00bee7ff has its CatchHandler @ 00aeeab8 */
  *param_2 = &PTR_FUN_00c8ec18;
  param_2[1] = uVar1;
  return;
}

~~~
