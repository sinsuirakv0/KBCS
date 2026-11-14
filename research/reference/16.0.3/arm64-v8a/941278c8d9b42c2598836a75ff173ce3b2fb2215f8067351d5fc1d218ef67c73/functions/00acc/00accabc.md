# 00accabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00accabc",
  "name": "FUN_00accabc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "82165e92b1bd63f45e815f18888727750414bae45669282811cd36dc887c9dce",
  "source_text_sha256": "82165e92b1bd63f45e815f18888727750414bae45669282811cd36dc887c9dce"
}
~~~

## 呼び出し元

- [007322cc](../00732/007322cc.md)
- [0093659c](../00936/0093659c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 399 bytes

~~~c

void FUN_00accabc(undefined8 *param_1,undefined4 param_2,undefined4 param_3)

{
  *param_1 = &PTR_FUN_00c8e960;
  *(undefined4 *)(param_1 + 1) = param_2;
  *(undefined4 *)((long)param_1 + 0xc) = param_3;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  *(undefined1 *)(param_1 + 5) = 1;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[10] = 0;
  return;
}

~~~
