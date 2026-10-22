# 00b7cbdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7cbdc.md)

## 関数情報

~~~json
{
  "address": "00b7cbdc",
  "name": "std::__ndk1::future<void>::future",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a15e1ea05dd121a21b6015a8a2613140eda7b2659b14e6a1b83504ca002a77a7",
  "source_text_sha256": "a15e1ea05dd121a21b6015a8a2613140eda7b2659b14e6a1b83504ca002a77a7"
}
~~~
## 呼び出し元

- [00bdb5d0](../00bdb/00bdb5d0.md)

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1a0](../00bdb/00bdb1a0.md)

## 疑似コード 1/1 / UTF-8 586 bytes

~~~c

/* std::__ndk1::future<void>::future(std::__ndk1::__assoc_sub_state*) */

void __thiscall std::__ndk1::future<void>::future(future<void> *this,__assoc_sub_state *param_1)

{
  uint uVar1;
  
  *(__assoc_sub_state **)this = param_1;
  mutex::lock((mutex *)(param_1 + 0x18));
  uVar1 = *(uint *)(param_1 + 0x70);
  if ((uVar1 >> 1 & 1) == 0) {
    FUN_00bd6d60(1,param_1 + 8);
    *(uint *)(param_1 + 0x70) = uVar1 | 2;
    mutex::unlock((mutex *)(param_1 + 0x18));
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(1);
}

~~~
