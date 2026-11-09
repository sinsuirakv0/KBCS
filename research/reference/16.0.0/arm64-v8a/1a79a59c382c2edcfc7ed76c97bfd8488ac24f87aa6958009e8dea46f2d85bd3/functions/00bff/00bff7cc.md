# 00bff7cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bff7cc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9be2bd443faab84ed7b31135866e848e6df90da16ed6a133379c3c225bc19ce",
  "source_text_sha256": "b9be2bd443faab84ed7b31135866e848e6df90da16ed6a133379c3c225bc19ce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 523 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv(long *param_1)

{
  uint *puVar1;
  uint uVar2;
  ulong uVar3;
  
  puVar1 = (uint *)param_1[3];
  if (puVar1 != (uint *)param_1[4]) {
    uVar2 = *puVar1;
    param_1[3] = (long)(puVar1 + 1);
    return (ulong)uVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bff7f8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar3 = (**(code **)(*param_1 + 0x50))(param_1);
  return uVar3;
}

~~~
