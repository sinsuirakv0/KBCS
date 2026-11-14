# 00acbd2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acbd2c",
  "name": "FUN_00acbd2c",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be207e4e7c2dee98c7044792ac07b38c173a6cb844ef96892887081ebd43a4b9",
  "source_text_sha256": "be207e4e7c2dee98c7044792ac07b38c173a6cb844ef96892887081ebd43a4b9"
}
~~~

## 呼び出し元

- [006af7a4](../006af/006af7a4.md)
- [00831ea0](../00831/00831ea0.md)

## 呼び出し先

- [0057c208](../0057c/0057c208.md)
- [00aca5f8](../00aca/00aca5f8.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acbd2c(long param_1,long *param_2)

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
  local_38 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)param_2[4];
  *(undefined1 *)(param_1 + 0xa0) = 1;
  *(undefined4 *)(param_1 + 0xa4) = 0;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_2) {
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057c208(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acbde0;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acbde0:
  FUN_00aca5f8(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
