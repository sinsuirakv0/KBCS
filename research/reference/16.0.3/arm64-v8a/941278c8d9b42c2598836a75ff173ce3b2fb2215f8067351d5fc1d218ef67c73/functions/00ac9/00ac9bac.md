# 00ac9bac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00ac9bac",
  "name": "FUN_00ac9bac",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c295b5f92822cc0bfbb173d61a5ffff5057a9ce2ded457e7a2dbce27cacbe1e",
  "source_text_sha256": "0c295b5f92822cc0bfbb173d61a5ffff5057a9ce2ded457e7a2dbce27cacbe1e"
}
~~~

## 呼び出し元

- [007890e0](../00789/007890e0.md)
- [0082fe24](../0082f/0082fe24.md)
- [008cbbc0](../008cb/008cbbc0.md)
- [00a735f8](../00a73/00a735f8.md)
- [00ac14b8](../00ac1/00ac14b8.md)

## 呼び出し先

- [0057c9b4](../0057c/0057c9b4.md)
- [008524fc](../00852/008524fc.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 1980 bytes

~~~c

void FUN_00ac9bac(long param_1,undefined4 param_2,undefined4 param_3,int param_4,long *param_5)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
                    /* try { // try from 00ac9bcc to 00bc9d2f has its CatchHandler @ 00ac9bcc
                       catch() { ... } // from try @ 00ac9bcc with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00ac9df0 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca06c with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca114 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca270 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca2fc with catch @ 00ac9bcc */
  local_38 = *(long *)(lVar1 + 0x28);
  *(bool *)(param_1 + 0x3c) = 1 < param_4;
  plVar2 = (long *)param_5[4];
  *(undefined4 *)(param_1 + 0x280) = param_3;
  *(int *)(param_1 + 0x5c) = param_4;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_5) {
    (**(code **)(*param_5 + 0x18))(param_5,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057c9b4(local_70,param_1 + 0x170);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00ac9c6c;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00ac9c6c:
  *(undefined4 *)(param_1 + 0x68) = param_2;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(lVar4 + 0x3570) = 0;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(lVar4 + 0x3573) = 0;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(param_1 + 0x3d) = 0;
  *(undefined1 *)(lVar4 + 0x3572) = 0;
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
