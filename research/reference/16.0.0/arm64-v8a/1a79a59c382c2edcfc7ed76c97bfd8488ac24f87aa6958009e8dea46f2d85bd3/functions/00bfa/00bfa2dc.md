# 00bfa2dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfa2dc",
  "name": "_ZNSt6__ndk16thread4joinEv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487",
  "source_text_sha256": "fd209afff0a20f7373e59b672e840269afd777fd3967356d13ffbdc2416e3487"
}
~~~

## 呼び出し元

- [00c57d70](../00c57/00c57d70.md)

## 呼び出し先

- [00c57d20](../00c57/00c57d20.md)
- [00c5d240](../00c5d/00c5d240.md)

## 関連文字列（未確認候補）

~~~text
"thread::join failed"
~~~

## 疑似コード / UTF-8 378 bytes

~~~c

void _ZNSt6__ndk16thread4joinEv(pthread_t *param_1)

{
  int iVar1;
  
  if (*param_1 == 0) {
    iVar1 = 0x16;
  }
  else {
    iVar1 = pthread_join(*param_1,(void **)0x0);
    if (iVar1 == 0) {
      *param_1 = 0;
      return;
    }
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(iVar1,"thread::join failed");
}

~~~
