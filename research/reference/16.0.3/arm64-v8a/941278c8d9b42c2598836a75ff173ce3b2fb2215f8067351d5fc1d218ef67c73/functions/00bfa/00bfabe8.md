# 00bfabe8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bfabe8",
  "name": "_ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "518f45d3fcb72c155ba6331ac3dcd23dc71faa4aff076c77bc87522b7102cb4c",
  "source_text_sha256": "518f45d3fcb72c155ba6331ac3dcd23dc71faa4aff076c77bc87522b7102cb4c"
}
~~~

## 呼び出し元

- [00c595c0](../00c59/00c595c0.md)

## 呼び出し先

- [0045aa34](../0045a/0045aa34.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c59180](../00c59/00c59180.md)
- [00c59190](../00c59/00c59190.md)

## 疑似コード / UTF-8 464 bytes

~~~c

void _ZNSt6__ndk16futureIvEC1EPNS_17__assoc_sub_stateE(long *param_1,long param_2)

{
  uint uVar1;
  
  *param_1 = param_2;
  _ZNSt6__ndk15mutex4lockEv(param_2 + 0x18);
  uVar1 = *(uint *)(param_2 + 0x70);
  if ((uVar1 >> 1 & 1) == 0) {
    FUN_00c54d60(1,param_2 + 8);
    *(uint *)(param_2 + 0x70) = uVar1 | 2;
    _ZNSt6__ndk15mutex6unlockEv(param_2 + 0x18);
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0045aa34(1);
}

~~~
