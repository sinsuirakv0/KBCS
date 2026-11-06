# 00aca4ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aca4ec",
  "name": "FUN_00aca4ec",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2a84721dadda7418adb96fce537c59feb2bbe1cbbc00e67367501dc33a6e0b9",
  "source_text_sha256": "a2a84721dadda7418adb96fce537c59feb2bbe1cbbc00e67367501dc33a6e0b9"
}
~~~

## 呼び出し元

- [00ab3338](../00ab3/00ab3338.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00aca4ec(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
