# 00bfa7ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bfa7ec",
  "name": "_ZNSt6__ndk16thread6detachEv",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8e133cc68e739b2283608f947ad481d46ceb7d2aadcb7c968af47c10216e317",
  "source_text_sha256": "e8e133cc68e739b2283608f947ad481d46ceb7d2aadcb7c968af47c10216e317"
}
~~~

## 呼び出し元

- [00c585e0](../00c58/00c585e0.md)

## 呼び出し先

- [00c581f0](../00c58/00c581f0.md)
- [00c5e350](../00c5e/00c5e350.md)

## 関連文字列（未確認候補）

~~~text
"thread::detach failed"
~~~

## 疑似コード / UTF-8 371 bytes

~~~c

void _ZNSt6__ndk16thread6detachEv(pthread_t *param_1)

{
  int iVar1;
  
  if (*param_1 == 0) {
    iVar1 = 0x16;
  }
  else {
    iVar1 = pthread_detach(*param_1);
    if (iVar1 == 0) {
      *param_1 = 0;
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"thread::detach failed");
}

~~~
