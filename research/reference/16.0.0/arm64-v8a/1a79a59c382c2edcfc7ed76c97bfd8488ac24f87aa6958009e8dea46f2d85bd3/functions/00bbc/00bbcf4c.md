# 00bbcf4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbcf4c",
  "name": "_ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cba34d5d671e8a26c9bfa9440cddde955aceabbada6c73a914dc97c465a7045c",
  "source_text_sha256": "cba34d5d671e8a26c9bfa9440cddde955aceabbada6c73a914dc97c465a7045c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 524 bytes

~~~c

void _ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBaseEPv
               (undefined8 param_1,undefined8 *param_2)

{
  if ((param_2 != (undefined8 *)0x0) && ((code *)*param_2 != (code *)0x0)) {
                    /* WARNING: Could not recover jumptable at 0x00bbcf5c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (*(code *)*param_2)(param_1,param_2[1]);
    return;
  }
  return;
}

~~~
