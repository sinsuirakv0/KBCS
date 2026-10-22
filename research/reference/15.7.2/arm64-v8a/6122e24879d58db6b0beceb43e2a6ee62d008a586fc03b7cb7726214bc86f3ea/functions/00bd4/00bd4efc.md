# 00bd4efc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bd4efc.md)

## 関数情報

~~~json
{
  "address": "00bd4efc",
  "name": "__cxa_allocate_exception",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0db61eabf0e743df10df7fa8f7502ceca63bbdadb555687e2a591f2b7a45ffd0",
  "source_text_sha256": "0db61eabf0e743df10df7fa8f7502ceca63bbdadb555687e2a591f2b7a45ffd0"
}
~~~
## 呼び出し元

- [00bdafa0](../00bda/00bdafa0.md)

## 呼び出し先

- [00bd56c8](../00bd5/00bd56c8.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdb140](../00bdb/00bdb140.md)

## 疑似コード 1/1 / UTF-8 1297 bytes

~~~c

long __cxa_allocate_exception(long param_1)

{
  void *__s;
  
  __s = (void *)FUN_00bd56c8(param_1 + 0x8fU & 0xfffffffffffffff0);
  if (__s != (void *)0x0) {
                    /* try { // try from 00bd4f2c to 00cd4f67 has its CatchHandler @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4f2c with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4f84 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4ffc with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd506c with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd50cc with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd50f0 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5178 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5240 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5330 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5408 with catch @ 00bd4f2c */
    memset(__s,0,param_1 + 0x8fU & 0xfffffffffffffff0);
    return (long)__s + 0x80;
  }
                    /* WARNING: Subroutine does not return */
  std::terminate();
}

~~~
