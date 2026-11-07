# 00aaae5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aaad50`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad50.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aaae5c",
  "name": "FUN_00aaae5c",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26273872dc40ca4b6e64cb8a0ba2ce92353d32cd87ee4dc5c2e384d58ae7e2ee",
  "source_text_sha256": "26273872dc40ca4b6e64cb8a0ba2ce92353d32cd87ee4dc5c2e384d58ae7e2ee"
}
~~~

## 呼び出し元

- [0059815c](../00598/0059815c.md)
- [00a7268c](../00a72/00a7268c.md)
- [00a7840c](../00a78/00a7840c.md)
- [00a788d0](../00a78/00a788d0.md)
- [00a80570](../00a80/00a80570.md)
- [00a823d8](../00a82/00a823d8.md)
- [00a8ac9c](../00a8a/00a8ac9c.md)
- [00a8b06c](../00a8b/00a8b06c.md)

## 呼び出し先

- [00bdb600](../00bdb/00bdb600.md)

## 疑似コード / UTF-8 382 bytes

~~~c

bool FUN_00aaae5c(long param_1,wchar_t param_2)

{
  wchar_t *pwVar1;
  wchar_t *pwVar2;
  
  pwVar2 = *(wchar_t **)(param_1 + 0x38);
  pwVar1 = wmemchr(*(wchar_t **)(param_1 + 0x30),param_2,
                   (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
  if (pwVar1 != (wchar_t *)0x0) {
    pwVar2 = pwVar1;
  }
  return pwVar2 == *(wchar_t **)(param_1 + 0x38);
}

~~~
