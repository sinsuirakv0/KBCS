# 00acbda4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00acbc98`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc98.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00acbda4",
  "name": "FUN_00acbda4",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aba472b56121b388ad8136ae7441e715cf47b40ef868e8d461d3d1d2ff058f25",
  "source_text_sha256": "aba472b56121b388ad8136ae7441e715cf47b40ef868e8d461d3d1d2ff058f25"
}
~~~

## 呼び出し元

- [00accf90](../00acc/00accf90.md)

## 呼び出し先

- [005533e0](../00553/005533e0.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetTop"
~~~

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00acbda4(void)

{
  long lVar1;
  char cVar2;
  undefined4 uVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  byte local_70 [16];
  void *local_60;
  byte local_58;
  char local_57 [7];
  char cStack_50;
  char acStack_4f [7];
  undefined1 local_48;
  undefined7 uStack_47;
  long local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)FUN_00565f94();
  uVar5 = FUN_00566284();
  local_58 = 0x1e;
  local_48 = 0;
  local_57[0] = s_getSafeInsetTop_002963ac[0];
  local_57[1] = s_getSafeInsetTop_002963ac[1];
  local_57[2] = s_getSafeInsetTop_002963ac[2];
  local_57[3] = s_getSafeInsetTop_002963ac[3];
  local_57[4] = s_getSafeInsetTop_002963ac[4];
  local_57[5] = s_getSafeInsetTop_002963ac[5];
  local_57[6] = s_getSafeInsetTop_002963ac[6];
  cStack_50 = s_getSafeInsetTop_002963ac[7];
  acStack_4f[0] = s_getSafeInsetTop_002963ac[8];
  acStack_4f[1] = s_getSafeInsetTop_002963ac[9];
  acStack_4f[2] = s_getSafeInsetTop_002963ac[10];
  acStack_4f[3] = s_getSafeInsetTop_002963ac[0xb];
  acStack_4f[4] = s_getSafeInsetTop_002963ac[0xc];
  acStack_4f[5] = s_getSafeInsetTop_002963ac[0xd];
  acStack_4f[6] = s_getSafeInsetTop_002963ac[0xe];
  local_70[0] = 6;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00566448(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT71(uStack_47,local_48));
  }
  uVar6 = FUN_0056626c(&local_40);
  if ((uVar6 & 1) != 0) {
    FUN_00566284();
    uVar5 = FUN_00566978();
    if (local_40 != 0) {
      uVar3 = FUN_005533e0(plVar4,uVar5);
      cVar2 = (**(code **)(*plVar4 + 0x720))(plVar4);
      if (cVar2 != '\0') {
        (**(code **)(*plVar4 + 0x80))(plVar4);
        (**(code **)(*plVar4 + 0x88))(plVar4);
      }
      goto LAB_00acbeac;
    }
  }
  uVar3 = 0;
LAB_00acbeac:
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar3);
  }
  return;
}

~~~
