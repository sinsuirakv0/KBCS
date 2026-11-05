# 00b7cbdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7cbdc.md)

## 関数情報

~~~json
{
  "address": "00b7cbdc",
  "name": "_ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6da5b9de47dcf212eb21c17e9a43563b83c4f90e38e2d1ce7addb9c34dcb0fcd",
  "source_text_sha256": "6da5b9de47dcf212eb21c17e9a43563b83c4f90e38e2d1ce7addb9c34dcb0fcd"
}
~~~
## 呼び出し元

- [00bdb5d0](../00bdb/00bdb5d0.md)

## 呼び出し先

- [004377fc](../00437/004377fc.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1a0](../00bdb/00bdb1a0.md)

## 疑似コード 1/1 / UTF-8 464 bytes

~~~c

void _ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE(long *param_1,long param_2)

{
  uint uVar1;
  
  *param_1 = param_2;
  _ZNSt6__ndk15mutex4lockEv(param_2 + 0x18);
  uVar1 = *(uint *)(param_2 + 0x70);
  if ((uVar1 >> 1 & 1) == 0) {
    FUN_00bd6d60(1,param_2 + 8);
    *(uint *)(param_2 + 0x70) = uVar1 | 2;
    _ZNSt6__ndk15mutex6unlockEv(param_2 + 0x18);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_004377fc(1);
}

~~~
