# 00b7cfbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7cfbc.md)

## 関数情報

~~~json
{
  "address": "00b7cfbc",
  "name": "std::__ndk1::promise<void>::set_value_at_thread_exit",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6972ace996bc94271d9179abffaa3c22ff567038b22e13a62f861b1f02cddce0",
  "source_text_sha256": "6972ace996bc94271d9179abffaa3c22ff567038b22e13a62f861b1f02cddce0"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00be1120](../00be1/00be1120.md)

## 疑似コード 1/1 / UTF-8 511 bytes

~~~c

/* std::__ndk1::promise<void>::set_value_at_thread_exit() */

void __thiscall std::__ndk1::promise<void>::set_value_at_thread_exit(promise<void> *this)

{
  if (*(__assoc_sub_state **)this != (__assoc_sub_state *)0x0) {
    __assoc_sub_state::set_value_at_thread_exit(*(__assoc_sub_state **)this);
    return;
  }
                    /* try { // try from 00b7cfd0 to 00c7d023 has its CatchHandler @ 00b7888c */
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(3);
}

~~~
