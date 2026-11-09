# 00bfa2bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfa2bc",
  "name": "_ZNSt6__ndk16threadD2Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160",
  "source_text_sha256": "f4a0dbf2c6ca2e59794e120809d6f08ac0e148e1fbe43a79561a00908594a160"
}
~~~

## 呼び出し元

- [00c57d80](../00c57/00c57d80.md)

## 呼び出し先

- [00c57c20](../00c57/00c57c20.md)

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZNSt6__ndk16threadD2Ev(long *param_1)

{
  if (*param_1 == 0) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
