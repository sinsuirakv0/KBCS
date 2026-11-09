# 00a6beec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a6beec",
  "name": "FUN_00a6beec",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e",
  "source_text_sha256": "ecd41032274546acef0255d0390cce71921150d0da6e21c420d9701b5696d81e"
}
~~~

## 呼び出し元

- [00a6a8d4](../00a6a/00a6a8d4.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)

## 疑似コード / UTF-8 443 bytes

~~~c

void FUN_00a6beec(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*(byte *)(param_2 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_2 + 8);
    uVar1 = *(undefined8 *)(param_2 + 0x18);
    param_1[1] = *(undefined8 *)(param_2 + 0x10);
    *param_1 = uVar2;
    param_1[2] = uVar1;
    return;
  }
  FUN_0043bae0(param_1,*(undefined8 *)(param_2 + 0x18),*(undefined8 *)(param_2 + 0x10));
  return;
}

~~~
