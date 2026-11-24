# 00bebbe4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0175.md#review-3cb88470aecc8e097bb9a27f8e5532b2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0003.md#review-3cb88470aecc8e097bb9a27f8e5532b2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebbe4",
  "name": "FUN_00bebbe4",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "65312db5a39fe3181047b0a1a04082fe8ff00ec24431f361275dff9074fef7e3",
  "source_text_sha256": "65312db5a39fe3181047b0a1a04082fe8ff00ec24431f361275dff9074fef7e3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebbe4",
        "00bebe83"
      ]
    ],
    "bytes_sha256": "21bd587518b391541712f8d40f3618c607d71147ff441eedbcf007456e89cb81",
    "instruction_count": 168,
    "instruction_bytes": 672,
    "body_bytes": 672,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be5088](../00be5/00be5088.md)

## 呼び出し先

- [00bebe84](../00beb/00bebe84.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4030 bytes

~~~c

bool FUN_00bebbe4(uint *param_1,uint *param_2)

{
  uint uVar1;
  long lVar2;
  uint uVar3;
  uint uVar4;
  ulong uVar5;
  int iVar6;
  uint uVar7;
  uint *puVar8;
  long lVar9;
  uint uVar10;
  uint *puVar11;
  uint *puVar12;
  long lVar13;
  uint *puVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 2;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      uVar4 = *param_1;
      uVar10 = param_1[1];
      uVar1 = param_2[-1];
      if (uVar4 <= uVar10) {
        if (uVar10 <= uVar1) {
          return true;
        }
        param_1[1] = uVar1;
        param_2[-1] = uVar10;
        uVar4 = *param_1;
        if (param_1[1] < uVar4) {
          *param_1 = param_1[1];
          param_1[1] = uVar4;
          return true;
        }
        return true;
      }
      if (uVar1 < uVar10) {
        *param_1 = uVar1;
      }
      else {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        if (uVar4 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00bebe58;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00bebe84(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bebc74;
    }
    uVar4 = *param_1;
    puVar12 = param_1 + 1;
    uVar10 = *puVar12;
    puVar8 = param_1 + 2;
    uVar1 = *puVar8;
    puVar11 = param_1;
    if (uVar10 < uVar4) {
      puVar14 = puVar8;
      uVar3 = uVar4;
      if (uVar10 <= uVar1) {
        *param_1 = uVar10;
        param_1[1] = uVar4;
        uVar10 = uVar1;
        puVar11 = puVar12;
        goto joined_r0x00bebdf0;
      }
    }
    else {
      uVar7 = uVar1;
      if (uVar10 <= uVar1) goto LAB_00bebe08;
      *puVar12 = uVar1;
      *puVar8 = uVar10;
      puVar14 = puVar12;
      uVar3 = uVar10;
joined_r0x00bebdf0:
      uVar7 = uVar10;
      if (uVar4 <= uVar1) goto LAB_00bebe08;
    }
    *puVar11 = uVar1;
    *puVar14 = uVar4;
    uVar7 = uVar3;
LAB_00bebe08:
    if (uVar7 <= param_2[-1]) {
      return true;
    }
    *puVar8 = param_2[-1];
    param_2[-1] = uVar7;
    uVar4 = *puVar8;
    uVar10 = *puVar12;
    if (uVar4 < uVar10) {
      uVar1 = *param_1;
      param_1[1] = uVar4;
      param_1[2] = uVar10;
      if (uVar4 < uVar1) {
        *param_1 = uVar4;
        param_1[1] = uVar1;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar5 < 2) {
    return true;
  }
  if (uVar5 == 2) {
    uVar4 = *param_1;
    if (uVar4 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00bebe58:
    param_2[-1] = uVar4;
    return true;
  }
LAB_00bebc74:
  uVar4 = *param_1;
  puVar8 = param_1 + 1;
  uVar10 = *puVar8;
  puVar12 = param_1 + 2;
  uVar1 = *puVar12;
  puVar11 = param_1;
  if (uVar10 < uVar4) {
    puVar14 = puVar12;
    if (uVar10 <= uVar1) {
      *param_1 = uVar10;
      param_1[1] = uVar4;
      puVar11 = puVar8;
      goto joined_r0x00bebd44;
    }
  }
  else {
    if (uVar10 <= uVar1) goto LAB_00bebd50;
    *puVar8 = uVar1;
    *puVar12 = uVar10;
    puVar14 = puVar8;
joined_r0x00bebd44:
    if (uVar4 <= uVar1) goto LAB_00bebd50;
  }
  *puVar11 = uVar1;
  *puVar14 = uVar4;
LAB_00bebd50:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 0xc;
    puVar11 = param_1 + 3;
    do {
      puVar8 = puVar11;
      uVar4 = *puVar8;
      uVar10 = *puVar12;
      lVar13 = lVar9;
      if (uVar4 < uVar10) {
        do {
          lVar2 = lVar13 + -4;
          *(uint *)((long)param_1 + lVar13) = uVar10;
          puVar11 = param_1;
          if (lVar2 == 0) goto LAB_00bebd6c;
          uVar10 = *(uint *)((long)param_1 + lVar13 + -8);
          lVar13 = lVar2;
        } while (uVar4 < uVar10);
        puVar11 = (uint *)((long)param_1 + lVar2);
LAB_00bebd6c:
        iVar6 = iVar6 + 1;
        *puVar11 = uVar4;
        if (iVar6 == 8) {
          return puVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 4;
      puVar11 = puVar8 + 1;
      puVar12 = puVar8;
    } while (puVar8 + 1 != param_2);
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bebbe4"></a> `00bebbe4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bebbe8"></a> `00bebbe8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bebbec"></a> `00bebbec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bebbf0"></a> `00bebbf0` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bebbf4"></a> `00bebbf4` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebbf8"></a> `00bebbf8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebbfc"></a> `00bebbfc` | `4c 01 00 54` | b.gt 0x00bebc24 | `CONDITIONAL_JUMP`
<a id="insn-00bebc00"></a> `00bebc00` | `23 13 00 54` | b.cc 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebc04"></a> `00bebc04` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebc08"></a> `00bebc08` | `61 03 00 54` | b.ne 0x00bebc74 | `CONDITIONAL_JUMP`
<a id="insn-00bebc0c"></a> `00bebc0c` | `29 c0 5f b8` | ldur w9,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebc10"></a> `00bebc10` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebc14"></a> `00bebc14` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebc18"></a> `00bebc18` | `62 12 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebc1c"></a> `00bebc1c` | `09 00 00 b9` | str w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebc20"></a> `00bebc20` | `8e 00 00 14` | b 0x00bebe58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc24"></a> `00bebc24` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bebc28"></a> `00bebc28` | `60 01 00 54` | b.eq 0x00bebc54 | `CONDITIONAL_JUMP`
<a id="insn-00bebc2c"></a> `00bebc2c` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bebc30"></a> `00bebc30` | `40 04 00 54` | b.eq 0x00bebcb8 | `CONDITIONAL_JUMP`
<a id="insn-00bebc34"></a> `00bebc34` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bebc38"></a> `00bebc38` | `e1 01 00 54` | b.ne 0x00bebc74 | `CONDITIONAL_JUMP`
<a id="insn-00bebc3c"></a> `00bebc3c` | `24 10 00 d1` | sub x4,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00bebc40"></a> `00bebc40` | `01 10 00 91` | add x1,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bebc44"></a> `00bebc44` | `02 20 00 91` | add x2,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bebc48"></a> `00bebc48` | `03 30 00 91` | add x3,x0,#0xc | `FALL_THROUGH`
<a id="insn-00bebc4c"></a> `00bebc4c` | `8e 00 00 94` | bl 0x00bebe84 | `UNCONDITIONAL_CALL`
<a id="insn-00bebc50"></a> `00bebc50` | `85 00 00 14` | b 0x00bebe64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc54"></a> `00bebc54` | `08 24 40 29` | ldp w8,w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebc58"></a> `00bebc58` | `2a c0 5f b8` | ldur w10,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebc5c"></a> `00bebc5c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebc60"></a> `00bebc60` | `22 05 00 54` | b.cs 0x00bebd04 | `CONDITIONAL_JUMP`
<a id="insn-00bebc64"></a> `00bebc64` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00bebc68"></a> `00bebc68` | `e2 0e 00 54` | b.cs 0x00bebe44 | `CONDITIONAL_JUMP`
<a id="insn-00bebc6c"></a> `00bebc6c` | `0a 00 00 b9` | str w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebc70"></a> `00bebc70` | `7a 00 00 14` | b 0x00bebe58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebc74"></a> `00bebc74` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bebc78"></a> `00bebc78` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebc7c"></a> `00bebc7c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bebc80"></a> `00bebc80` | `4c 4d 40 b8` | ldr w12,[x10, #0x4]! | `FALL_THROUGH`
<a id="insn-00bebc84"></a> `00bebc84` | `69 8d 40 b8` | ldr w9,[x11, #0x8]! | `FALL_THROUGH`
<a id="insn-00bebc88"></a> `00bebc88` | `9f 01 08 6b` | cmp w12,w8 | `FALL_THROUGH`
<a id="insn-00bebc8c"></a> `00bebc8c` | `e2 04 00 54` | b.cs 0x00bebd28 | `CONDITIONAL_JUMP`
<a id="insn-00bebc90"></a> `00bebc90` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00bebc94"></a> `00bebc94` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bebc98"></a> `00bebc98` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bebc9c"></a> `00bebc9c` | `63 05 00 54` | b.cc 0x00bebd48 | `CONDITIONAL_JUMP`
<a id="insn-00bebca0"></a> `00bebca0` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebca4"></a> `00bebca4` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00bebca8"></a> `00bebca8` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bebcac"></a> `00bebcac` | `0c 20 00 29` | stp w12,w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebcb0"></a> `00bebcb0` | `c3 04 00 54` | b.cc 0x00bebd48 | `CONDITIONAL_JUMP`
<a id="insn-00bebcb4"></a> `00bebcb4` | `27 00 00 14` | b 0x00bebd50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebcb8"></a> `00bebcb8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bebcbc"></a> `00bebcbc` | `0b 00 40 b9` | ldr w11,[x0] | `FALL_THROUGH`
<a id="insn-00bebcc0"></a> `00bebcc0` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bebcc4"></a> `00bebcc4` | `0a 4d 40 b8` | ldr w10,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bebcc8"></a> `00bebcc8` | `2c 8d 40 b8` | ldr w12,[x9, #0x8]! | `FALL_THROUGH`
<a id="insn-00bebccc"></a> `00bebccc` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bebcd0"></a> `00bebcd0` | `02 08 00 54` | b.cs 0x00bebdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bebcd4"></a> `00bebcd4` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bebcd8"></a> `00bebcd8` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bebcdc"></a> `00bebcdc` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bebce0"></a> `00bebce0` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00bebce4"></a> `00bebce4` | `83 08 00 54` | b.cc 0x00bebdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bebce8"></a> `00bebce8` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00bebcec"></a> `00bebcec` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00bebcf0"></a> `00bebcf0` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bebcf4"></a> `00bebcf4` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00bebcf8"></a> `00bebcf8` | `0a 2c 00 29` | stp w10,w11,[x0] | `FALL_THROUGH`
<a id="insn-00bebcfc"></a> `00bebcfc` | `c3 07 00 54` | b.cc 0x00bebdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bebd00"></a> `00bebd00` | `41 00 00 14` | b 0x00bebe04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebd04"></a> `00bebd04` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00bebd08"></a> `00bebd08` | `e2 0a 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebd0c"></a> `00bebd0c` | `0a 04 00 b9` | str w10,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bebd10"></a> `00bebd10` | `29 c0 1f b8` | stur w9,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebd14"></a> `00bebd14` | `08 24 40 29` | ldp w8,w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebd18"></a> `00bebd18` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebd1c"></a> `00bebd1c` | `42 0a 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebd20"></a> `00bebd20` | `09 20 00 29` | stp w9,w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebd24"></a> `00bebd24` | `50 00 00 14` | b 0x00bebe64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebd28"></a> `00bebd28` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00bebd2c"></a> `00bebd2c` | `22 01 00 54` | b.cs 0x00bebd50 | `CONDITIONAL_JUMP`
<a id="insn-00bebd30"></a> `00bebd30` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebd34"></a> `00bebd34` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bebd38"></a> `00bebd38` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bebd3c"></a> `00bebd3c` | `49 01 00 b9` | str w9,[x10] | `FALL_THROUGH`
<a id="insn-00bebd40"></a> `00bebd40` | `6c 01 00 b9` | str w12,[x11] | `FALL_THROUGH`
<a id="insn-00bebd44"></a> `00bebd44` | `62 00 00 54` | b.cs 0x00bebd50 | `CONDITIONAL_JUMP`
<a id="insn-00bebd48"></a> `00bebd48` | `a9 01 00 b9` | str w9,[x13] | `FALL_THROUGH`
<a id="insn-00bebd4c"></a> `00bebd4c` | `c8 01 00 b9` | str w8,[x14] | `FALL_THROUGH`
<a id="insn-00bebd50"></a> `00bebd50` | `08 30 00 91` | add x8,x0,#0xc | `FALL_THROUGH`
<a id="insn-00bebd54"></a> `00bebd54` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bebd58"></a> `00bebd58` | `60 08 00 54` | b.eq 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebd5c"></a> `00bebd5c` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00bebd60"></a> `00bebd60` | `8a 01 80 52` | mov w10,#0xc | `FALL_THROUGH`
<a id="insn-00bebd64"></a> `00bebd64` | `0c 00 00 14` | b 0x00bebd94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebd68"></a> `00bebd68` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bebd6c"></a> `00bebd6c` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bebd70"></a> `00bebd70` | `6c 01 00 b9` | str w12,[x11] | `FALL_THROUGH`
<a id="insn-00bebd74"></a> `00bebd74` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bebd78"></a> `00bebd78` | `e0 07 00 54` | b.eq 0x00bebe74 | `CONDITIONAL_JUMP`
<a id="insn-00bebd7c"></a> `00bebd7c` | `0c 11 00 91` | add x12,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bebd80"></a> `00bebd80` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bebd84"></a> `00bebd84` | `4a 11 00 91` | add x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bebd88"></a> `00bebd88` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bebd8c"></a> `00bebd8c` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00bebd90"></a> `00bebd90` | `a0 06 00 54` | b.eq 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebd94"></a> `00bebd94` | `0c 01 40 b9` | ldr w12,[x8] | `FALL_THROUGH`
<a id="insn-00bebd98"></a> `00bebd98` | `6b 01 40 b9` | ldr w11,[x11] | `FALL_THROUGH`
<a id="insn-00bebd9c"></a> `00bebd9c` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00bebda0"></a> `00bebda0` | `e2 fe ff 54` | b.cs 0x00bebd7c | `CONDITIONAL_JUMP`
<a id="insn-00bebda4"></a> `00bebda4` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bebda8"></a> `00bebda8` | `cd 11 00 f1` | subs x13,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bebdac"></a> `00bebdac` | `0b 68 2e b8` | str w11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bebdb0"></a> `00bebdb0` | `c0 fd ff 54` | b.eq 0x00bebd68 | `CONDITIONAL_JUMP`
<a id="insn-00bebdb4"></a> `00bebdb4` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00bebdb8"></a> `00bebdb8` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00bebdbc"></a> `00bebdbc` | `6b 81 5f b8` | ldur w11,[x11, #-0x8] | `FALL_THROUGH`
<a id="insn-00bebdc0"></a> `00bebdc0` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00bebdc4"></a> `00bebdc4` | `23 ff ff 54` | b.cc 0x00bebda8 | `CONDITIONAL_JUMP`
<a id="insn-00bebdc8"></a> `00bebdc8` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00bebdcc"></a> `00bebdcc` | `e8 ff ff 17` | b 0x00bebd6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bebdd0"></a> `00bebdd0` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bebdd4"></a> `00bebdd4` | `82 01 00 54` | b.cs 0x00bebe04 | `CONDITIONAL_JUMP`
<a id="insn-00bebdd8"></a> `00bebdd8` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00bebddc"></a> `00bebddc` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bebde0"></a> `00bebde0` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00bebde4"></a> `00bebde4` | `e2 03 0a 2a` | mov w2,w10 | `FALL_THROUGH`
<a id="insn-00bebde8"></a> `00bebde8` | `0c 01 00 b9` | str w12,[x8] | `FALL_THROUGH`
<a id="insn-00bebdec"></a> `00bebdec` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00bebdf0"></a> `00bebdf0` | `c2 00 00 54` | b.cs 0x00bebe08 | `CONDITIONAL_JUMP`
<a id="insn-00bebdf4"></a> `00bebdf4` | `ea 03 02 2a` | mov w10,w2 | `FALL_THROUGH`
<a id="insn-00bebdf8"></a> `00bebdf8` | `ac 01 00 b9` | str w12,[x13] | `FALL_THROUGH`
<a id="insn-00bebdfc"></a> `00bebdfc` | `cb 01 00 b9` | str w11,[x14] | `FALL_THROUGH`
<a id="insn-00bebe00"></a> `00bebe00` | `02 00 00 14` | b 0x00bebe08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebe04"></a> `00bebe04` | `ea 03 0c 2a` | mov w10,w12 | `FALL_THROUGH`
<a id="insn-00bebe08"></a> `00bebe08` | `2b c0 5f b8` | ldur w11,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebe0c"></a> `00bebe0c` | `7f 01 0a 6b` | cmp w11,w10 | `FALL_THROUGH`
<a id="insn-00bebe10"></a> `00bebe10` | `a2 02 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebe14"></a> `00bebe14` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00bebe18"></a> `00bebe18` | `2a c0 1f b8` | stur w10,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebe1c"></a> `00bebe1c` | `29 01 40 b9` | ldr w9,[x9] | `FALL_THROUGH`
<a id="insn-00bebe20"></a> `00bebe20` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00bebe24"></a> `00bebe24` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebe28"></a> `00bebe28` | `e2 01 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebe2c"></a> `00bebe2c` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebe30"></a> `00bebe30` | `09 a0 00 29` | stp w9,w8,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bebe34"></a> `00bebe34` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bebe38"></a> `00bebe38` | `62 01 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebe3c"></a> `00bebe3c` | `09 28 00 29` | stp w9,w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebe40"></a> `00bebe40` | `09 00 00 14` | b 0x00bebe64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebe44"></a> `00bebe44` | `09 20 00 29` | stp w9,w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebe48"></a> `00bebe48` | `29 c0 5f b8` | ldur w9,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebe4c"></a> `00bebe4c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bebe50"></a> `00bebe50` | `a2 00 00 54` | b.cs 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebe54"></a> `00bebe54` | `09 04 00 b9` | str w9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bebe58"></a> `00bebe58` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bebe5c"></a> `00bebe5c` | `28 c0 1f b8` | stur w8,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebe60"></a> `00bebe60` | `02 00 00 14` | b 0x00bebe68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebe64"></a> `00bebe64` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bebe68"></a> `00bebe68` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bebe6c"></a> `00bebe6c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bebe70"></a> `00bebe70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bebe74"></a> `00bebe74` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bebe78"></a> `00bebe78` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bebe7c"></a> `00bebe7c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bebe80"></a> `00bebe80` | `fa ff ff 17` | b 0x00bebe68 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bebbe4`](#insn-00bebbe4) 範囲 `[['00bebbe4', '00bebbff']]`
  - `CONDITIONAL_JUMP` [`00bebbfc`](#insn-00bebbfc) → [`00bebc24`](#insn-00bebc24)
  - `FALL_THROUGH` [`00bebbfc`](#insn-00bebbfc) → [`00bebc00`](#insn-00bebc00)
- ブロック [`00bebc00`](#insn-00bebc00) 範囲 `[['00bebc00', '00bebc03']]`
  - `CONDITIONAL_JUMP` [`00bebc00`](#insn-00bebc00) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebc00`](#insn-00bebc00) → [`00bebc04`](#insn-00bebc04)
- ブロック [`00bebc04`](#insn-00bebc04) 範囲 `[['00bebc04', '00bebc0b']]`
  - `CONDITIONAL_JUMP` [`00bebc08`](#insn-00bebc08) → [`00bebc74`](#insn-00bebc74)
  - `FALL_THROUGH` [`00bebc08`](#insn-00bebc08) → [`00bebc0c`](#insn-00bebc0c)
- ブロック [`00bebc0c`](#insn-00bebc0c) 範囲 `[['00bebc0c', '00bebc1b']]`
  - `CONDITIONAL_JUMP` [`00bebc18`](#insn-00bebc18) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebc18`](#insn-00bebc18) → [`00bebc1c`](#insn-00bebc1c)
- ブロック [`00bebc1c`](#insn-00bebc1c) 範囲 `[['00bebc1c', '00bebc23']]`
  - `UNCONDITIONAL_JUMP` [`00bebc20`](#insn-00bebc20) → [`00bebe58`](#insn-00bebe58)
- ブロック [`00bebc24`](#insn-00bebc24) 範囲 `[['00bebc24', '00bebc2b']]`
  - `CONDITIONAL_JUMP` [`00bebc28`](#insn-00bebc28) → [`00bebc54`](#insn-00bebc54)
  - `FALL_THROUGH` [`00bebc28`](#insn-00bebc28) → [`00bebc2c`](#insn-00bebc2c)
- ブロック [`00bebc2c`](#insn-00bebc2c) 範囲 `[['00bebc2c', '00bebc33']]`
  - `CONDITIONAL_JUMP` [`00bebc30`](#insn-00bebc30) → [`00bebcb8`](#insn-00bebcb8)
  - `FALL_THROUGH` [`00bebc30`](#insn-00bebc30) → [`00bebc34`](#insn-00bebc34)
- ブロック [`00bebc34`](#insn-00bebc34) 範囲 `[['00bebc34', '00bebc3b']]`
  - `CONDITIONAL_JUMP` [`00bebc38`](#insn-00bebc38) → [`00bebc74`](#insn-00bebc74)
  - `FALL_THROUGH` [`00bebc38`](#insn-00bebc38) → [`00bebc3c`](#insn-00bebc3c)
- ブロック [`00bebc3c`](#insn-00bebc3c) 範囲 `[['00bebc3c', '00bebc53']]`
  - `UNCONDITIONAL_JUMP` [`00bebc50`](#insn-00bebc50) → [`00bebe64`](#insn-00bebe64)
- ブロック [`00bebc54`](#insn-00bebc54) 範囲 `[['00bebc54', '00bebc63']]`
  - `CONDITIONAL_JUMP` [`00bebc60`](#insn-00bebc60) → [`00bebd04`](#insn-00bebd04)
  - `FALL_THROUGH` [`00bebc60`](#insn-00bebc60) → [`00bebc64`](#insn-00bebc64)
- ブロック [`00bebc64`](#insn-00bebc64) 範囲 `[['00bebc64', '00bebc6b']]`
  - `CONDITIONAL_JUMP` [`00bebc68`](#insn-00bebc68) → [`00bebe44`](#insn-00bebe44)
  - `FALL_THROUGH` [`00bebc68`](#insn-00bebc68) → [`00bebc6c`](#insn-00bebc6c)
- ブロック [`00bebc6c`](#insn-00bebc6c) 範囲 `[['00bebc6c', '00bebc73']]`
  - `UNCONDITIONAL_JUMP` [`00bebc70`](#insn-00bebc70) → [`00bebe58`](#insn-00bebe58)
- ブロック [`00bebc74`](#insn-00bebc74) 範囲 `[['00bebc74', '00bebc8f']]`
  - `CONDITIONAL_JUMP` [`00bebc8c`](#insn-00bebc8c) → [`00bebd28`](#insn-00bebd28)
  - `FALL_THROUGH` [`00bebc8c`](#insn-00bebc8c) → [`00bebc90`](#insn-00bebc90)
- ブロック [`00bebc90`](#insn-00bebc90) 範囲 `[['00bebc90', '00bebc9f']]`
  - `CONDITIONAL_JUMP` [`00bebc9c`](#insn-00bebc9c) → [`00bebd48`](#insn-00bebd48)
  - `FALL_THROUGH` [`00bebc9c`](#insn-00bebc9c) → [`00bebca0`](#insn-00bebca0)
- ブロック [`00bebca0`](#insn-00bebca0) 範囲 `[['00bebca0', '00bebcb3']]`
  - `CONDITIONAL_JUMP` [`00bebcb0`](#insn-00bebcb0) → [`00bebd48`](#insn-00bebd48)
  - `FALL_THROUGH` [`00bebcb0`](#insn-00bebcb0) → [`00bebcb4`](#insn-00bebcb4)
- ブロック [`00bebcb4`](#insn-00bebcb4) 範囲 `[['00bebcb4', '00bebcb7']]`
  - `UNCONDITIONAL_JUMP` [`00bebcb4`](#insn-00bebcb4) → [`00bebd50`](#insn-00bebd50)
- ブロック [`00bebcb8`](#insn-00bebcb8) 範囲 `[['00bebcb8', '00bebcd3']]`
  - `CONDITIONAL_JUMP` [`00bebcd0`](#insn-00bebcd0) → [`00bebdd0`](#insn-00bebdd0)
  - `FALL_THROUGH` [`00bebcd0`](#insn-00bebcd0) → [`00bebcd4`](#insn-00bebcd4)
- ブロック [`00bebcd4`](#insn-00bebcd4) 範囲 `[['00bebcd4', '00bebce7']]`
  - `CONDITIONAL_JUMP` [`00bebce4`](#insn-00bebce4) → [`00bebdf4`](#insn-00bebdf4)
  - `FALL_THROUGH` [`00bebce4`](#insn-00bebce4) → [`00bebce8`](#insn-00bebce8)
- ブロック [`00bebce8`](#insn-00bebce8) 範囲 `[['00bebce8', '00bebcff']]`
  - `CONDITIONAL_JUMP` [`00bebcfc`](#insn-00bebcfc) → [`00bebdf4`](#insn-00bebdf4)
  - `FALL_THROUGH` [`00bebcfc`](#insn-00bebcfc) → [`00bebd00`](#insn-00bebd00)
- ブロック [`00bebd00`](#insn-00bebd00) 範囲 `[['00bebd00', '00bebd03']]`
  - `UNCONDITIONAL_JUMP` [`00bebd00`](#insn-00bebd00) → [`00bebe04`](#insn-00bebe04)
- ブロック [`00bebd04`](#insn-00bebd04) 範囲 `[['00bebd04', '00bebd0b']]`
  - `CONDITIONAL_JUMP` [`00bebd08`](#insn-00bebd08) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebd08`](#insn-00bebd08) → [`00bebd0c`](#insn-00bebd0c)
- ブロック [`00bebd0c`](#insn-00bebd0c) 範囲 `[['00bebd0c', '00bebd1f']]`
  - `CONDITIONAL_JUMP` [`00bebd1c`](#insn-00bebd1c) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebd1c`](#insn-00bebd1c) → [`00bebd20`](#insn-00bebd20)
- ブロック [`00bebd20`](#insn-00bebd20) 範囲 `[['00bebd20', '00bebd27']]`
  - `UNCONDITIONAL_JUMP` [`00bebd24`](#insn-00bebd24) → [`00bebe64`](#insn-00bebe64)
- ブロック [`00bebd28`](#insn-00bebd28) 範囲 `[['00bebd28', '00bebd2f']]`
  - `CONDITIONAL_JUMP` [`00bebd2c`](#insn-00bebd2c) → [`00bebd50`](#insn-00bebd50)
  - `FALL_THROUGH` [`00bebd2c`](#insn-00bebd2c) → [`00bebd30`](#insn-00bebd30)
- ブロック [`00bebd30`](#insn-00bebd30) 範囲 `[['00bebd30', '00bebd47']]`
  - `CONDITIONAL_JUMP` [`00bebd44`](#insn-00bebd44) → [`00bebd50`](#insn-00bebd50)
  - `FALL_THROUGH` [`00bebd44`](#insn-00bebd44) → [`00bebd48`](#insn-00bebd48)
- ブロック [`00bebd48`](#insn-00bebd48) 範囲 `[['00bebd48', '00bebd4f']]`
  - `FALL_THROUGH` [`00bebd4c`](#insn-00bebd4c) → [`00bebd50`](#insn-00bebd50)
- ブロック [`00bebd50`](#insn-00bebd50) 範囲 `[['00bebd50', '00bebd5b']]`
  - `CONDITIONAL_JUMP` [`00bebd58`](#insn-00bebd58) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebd58`](#insn-00bebd58) → [`00bebd5c`](#insn-00bebd5c)
- ブロック [`00bebd5c`](#insn-00bebd5c) 範囲 `[['00bebd5c', '00bebd67']]`
  - `UNCONDITIONAL_JUMP` [`00bebd64`](#insn-00bebd64) → [`00bebd94`](#insn-00bebd94)
- ブロック [`00bebd68`](#insn-00bebd68) 範囲 `[['00bebd68', '00bebd6b']]`
  - `FALL_THROUGH` [`00bebd68`](#insn-00bebd68) → [`00bebd6c`](#insn-00bebd6c)
- ブロック [`00bebd6c`](#insn-00bebd6c) 範囲 `[['00bebd6c', '00bebd7b']]`
  - `CONDITIONAL_JUMP` [`00bebd78`](#insn-00bebd78) → [`00bebe74`](#insn-00bebe74)
  - `FALL_THROUGH` [`00bebd78`](#insn-00bebd78) → [`00bebd7c`](#insn-00bebd7c)
- ブロック [`00bebd7c`](#insn-00bebd7c) 範囲 `[['00bebd7c', '00bebd93']]`
  - `CONDITIONAL_JUMP` [`00bebd90`](#insn-00bebd90) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebd90`](#insn-00bebd90) → [`00bebd94`](#insn-00bebd94)
- ブロック [`00bebd94`](#insn-00bebd94) 範囲 `[['00bebd94', '00bebda3']]`
  - `CONDITIONAL_JUMP` [`00bebda0`](#insn-00bebda0) → [`00bebd7c`](#insn-00bebd7c)
  - `FALL_THROUGH` [`00bebda0`](#insn-00bebda0) → [`00bebda4`](#insn-00bebda4)
- ブロック [`00bebda4`](#insn-00bebda4) 範囲 `[['00bebda4', '00bebda7']]`
  - `FALL_THROUGH` [`00bebda4`](#insn-00bebda4) → [`00bebda8`](#insn-00bebda8)
- ブロック [`00bebda8`](#insn-00bebda8) 範囲 `[['00bebda8', '00bebdb3']]`
  - `CONDITIONAL_JUMP` [`00bebdb0`](#insn-00bebdb0) → [`00bebd68`](#insn-00bebd68)
  - `FALL_THROUGH` [`00bebdb0`](#insn-00bebdb0) → [`00bebdb4`](#insn-00bebdb4)
- ブロック [`00bebdb4`](#insn-00bebdb4) 範囲 `[['00bebdb4', '00bebdc7']]`
  - `CONDITIONAL_JUMP` [`00bebdc4`](#insn-00bebdc4) → [`00bebda8`](#insn-00bebda8)
  - `FALL_THROUGH` [`00bebdc4`](#insn-00bebdc4) → [`00bebdc8`](#insn-00bebdc8)
- ブロック [`00bebdc8`](#insn-00bebdc8) 範囲 `[['00bebdc8', '00bebdcf']]`
  - `UNCONDITIONAL_JUMP` [`00bebdcc`](#insn-00bebdcc) → [`00bebd6c`](#insn-00bebd6c)
- ブロック [`00bebdd0`](#insn-00bebdd0) 範囲 `[['00bebdd0', '00bebdd7']]`
  - `CONDITIONAL_JUMP` [`00bebdd4`](#insn-00bebdd4) → [`00bebe04`](#insn-00bebe04)
  - `FALL_THROUGH` [`00bebdd4`](#insn-00bebdd4) → [`00bebdd8`](#insn-00bebdd8)
- ブロック [`00bebdd8`](#insn-00bebdd8) 範囲 `[['00bebdd8', '00bebdf3']]`
  - `CONDITIONAL_JUMP` [`00bebdf0`](#insn-00bebdf0) → [`00bebe08`](#insn-00bebe08)
  - `FALL_THROUGH` [`00bebdf0`](#insn-00bebdf0) → [`00bebdf4`](#insn-00bebdf4)
- ブロック [`00bebdf4`](#insn-00bebdf4) 範囲 `[['00bebdf4', '00bebe03']]`
  - `UNCONDITIONAL_JUMP` [`00bebe00`](#insn-00bebe00) → [`00bebe08`](#insn-00bebe08)
- ブロック [`00bebe04`](#insn-00bebe04) 範囲 `[['00bebe04', '00bebe07']]`
  - `FALL_THROUGH` [`00bebe04`](#insn-00bebe04) → [`00bebe08`](#insn-00bebe08)
- ブロック [`00bebe08`](#insn-00bebe08) 範囲 `[['00bebe08', '00bebe13']]`
  - `CONDITIONAL_JUMP` [`00bebe10`](#insn-00bebe10) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe10`](#insn-00bebe10) → [`00bebe14`](#insn-00bebe14)
- ブロック [`00bebe14`](#insn-00bebe14) 範囲 `[['00bebe14', '00bebe2b']]`
  - `CONDITIONAL_JUMP` [`00bebe28`](#insn-00bebe28) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe28`](#insn-00bebe28) → [`00bebe2c`](#insn-00bebe2c)
- ブロック [`00bebe2c`](#insn-00bebe2c) 範囲 `[['00bebe2c', '00bebe3b']]`
  - `CONDITIONAL_JUMP` [`00bebe38`](#insn-00bebe38) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe38`](#insn-00bebe38) → [`00bebe3c`](#insn-00bebe3c)
- ブロック [`00bebe3c`](#insn-00bebe3c) 範囲 `[['00bebe3c', '00bebe43']]`
  - `UNCONDITIONAL_JUMP` [`00bebe40`](#insn-00bebe40) → [`00bebe64`](#insn-00bebe64)
- ブロック [`00bebe44`](#insn-00bebe44) 範囲 `[['00bebe44', '00bebe53']]`
  - `CONDITIONAL_JUMP` [`00bebe50`](#insn-00bebe50) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe50`](#insn-00bebe50) → [`00bebe54`](#insn-00bebe54)
- ブロック [`00bebe54`](#insn-00bebe54) 範囲 `[['00bebe54', '00bebe57']]`
  - `FALL_THROUGH` [`00bebe54`](#insn-00bebe54) → [`00bebe58`](#insn-00bebe58)
- ブロック [`00bebe58`](#insn-00bebe58) 範囲 `[['00bebe58', '00bebe63']]`
  - `UNCONDITIONAL_JUMP` [`00bebe60`](#insn-00bebe60) → [`00bebe68`](#insn-00bebe68)
- ブロック [`00bebe64`](#insn-00bebe64) 範囲 `[['00bebe64', '00bebe67']]`
  - `FALL_THROUGH` [`00bebe64`](#insn-00bebe64) → [`00bebe68`](#insn-00bebe68)
- ブロック [`00bebe68`](#insn-00bebe68) 範囲 `[['00bebe68', '00bebe73']]`
- ブロック [`00bebe74`](#insn-00bebe74) 範囲 `[['00bebe74', '00bebe83']]`
  - `UNCONDITIONAL_JUMP` [`00bebe80`](#insn-00bebe80) → [`00bebe68`](#insn-00bebe68)

## 命令位置別の参照

- [`00bebbe8`](#insn-00bebbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebbfc`](#insn-00bebbfc) → [`00bebc24`](#insn-00bebc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc00`](#insn-00bebc00) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc08`](#insn-00bebc08) → [`00bebc74`](#insn-00bebc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc18`](#insn-00bebc18) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc20`](#insn-00bebc20) → [`00bebe58`](#insn-00bebe58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc28`](#insn-00bebc28) → [`00bebc54`](#insn-00bebc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc30`](#insn-00bebc30) → [`00bebcb8`](#insn-00bebcb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc38`](#insn-00bebc38) → [`00bebc74`](#insn-00bebc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc4c`](#insn-00bebc4c) → [`00bebe84`](00bebe84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bebe84` · 推定シンボル `None` · 推定型 `None`
- [`00bebc50`](#insn-00bebc50) → [`00bebe64`](#insn-00bebe64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc60`](#insn-00bebc60) → [`00bebd04`](#insn-00bebd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc68`](#insn-00bebc68) → [`00bebe44`](#insn-00bebe44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc70`](#insn-00bebc70) → [`00bebe58`](#insn-00bebe58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc8c`](#insn-00bebc8c) → [`00bebd28`](#insn-00bebd28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebc9c`](#insn-00bebc9c) → [`00bebd48`](#insn-00bebd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcb0`](#insn-00bebcb0) → [`00bebd48`](#insn-00bebd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcb4`](#insn-00bebcb4) → [`00bebd50`](#insn-00bebd50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcd0`](#insn-00bebcd0) → [`00bebdd0`](#insn-00bebdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebce4`](#insn-00bebce4) → [`00bebdf4`](#insn-00bebdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebcfc`](#insn-00bebcfc) → [`00bebdf4`](#insn-00bebdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd00`](#insn-00bebd00) → [`00bebe04`](#insn-00bebe04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd08`](#insn-00bebd08) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd1c`](#insn-00bebd1c) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd24`](#insn-00bebd24) → [`00bebe64`](#insn-00bebe64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd2c`](#insn-00bebd2c) → [`00bebd50`](#insn-00bebd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd44`](#insn-00bebd44) → [`00bebd50`](#insn-00bebd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd58`](#insn-00bebd58) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd64`](#insn-00bebd64) → [`00bebd94`](#insn-00bebd94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd78`](#insn-00bebd78) → [`00bebe74`](#insn-00bebe74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebd90`](#insn-00bebd90) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebda0`](#insn-00bebda0) → [`00bebd7c`](#insn-00bebd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdb0`](#insn-00bebdb0) → [`00bebd68`](#insn-00bebd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdc4`](#insn-00bebdc4) → [`00bebda8`](#insn-00bebda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdcc`](#insn-00bebdcc) → [`00bebd6c`](#insn-00bebd6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdd4`](#insn-00bebdd4) → [`00bebe04`](#insn-00bebe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdf0`](#insn-00bebdf0) → [`00bebe08`](#insn-00bebe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe00`](#insn-00bebe00) → [`00bebe08`](#insn-00bebe08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe10`](#insn-00bebe10) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe28`](#insn-00bebe28) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe38`](#insn-00bebe38) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe40`](#insn-00bebe40) → [`00bebe64`](#insn-00bebe64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe50`](#insn-00bebe50) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe60`](#insn-00bebe60) → [`00bebe68`](#insn-00bebe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe68`](#insn-00bebe68) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe80`](#insn-00bebe80) → [`00bebe68`](#insn-00bebe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bebbe8`](#insn-00bebbe8)

~~~json
{
  "source": "00bebbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebbfc`](#insn-00bebbfc)

~~~json
{
  "source": "00bebbfc",
  "target": "00bebc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc00`](#insn-00bebc00)

~~~json
{
  "source": "00bebc00",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc08`](#insn-00bebc08)

~~~json
{
  "source": "00bebc08",
  "target": "00bebc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc18`](#insn-00bebc18)

~~~json
{
  "source": "00bebc18",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc20`](#insn-00bebc20)

~~~json
{
  "source": "00bebc20",
  "target": "00bebe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc28`](#insn-00bebc28)

~~~json
{
  "source": "00bebc28",
  "target": "00bebc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc30`](#insn-00bebc30)

~~~json
{
  "source": "00bebc30",
  "target": "00bebcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc38`](#insn-00bebc38)

~~~json
{
  "source": "00bebc38",
  "target": "00bebc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc4c`](#insn-00bebc4c)

~~~json
{
  "source": "00bebc4c",
  "target": "00bebe84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bebc50`](#insn-00bebc50)

~~~json
{
  "source": "00bebc50",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc60`](#insn-00bebc60)

~~~json
{
  "source": "00bebc60",
  "target": "00bebd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc68`](#insn-00bebc68)

~~~json
{
  "source": "00bebc68",
  "target": "00bebe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc70`](#insn-00bebc70)

~~~json
{
  "source": "00bebc70",
  "target": "00bebe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc8c`](#insn-00bebc8c)

~~~json
{
  "source": "00bebc8c",
  "target": "00bebd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebc9c`](#insn-00bebc9c)

~~~json
{
  "source": "00bebc9c",
  "target": "00bebd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcb0`](#insn-00bebcb0)

~~~json
{
  "source": "00bebcb0",
  "target": "00bebd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcb4`](#insn-00bebcb4)

~~~json
{
  "source": "00bebcb4",
  "target": "00bebd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcd0`](#insn-00bebcd0)

~~~json
{
  "source": "00bebcd0",
  "target": "00bebdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebce4`](#insn-00bebce4)

~~~json
{
  "source": "00bebce4",
  "target": "00bebdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebcfc`](#insn-00bebcfc)

~~~json
{
  "source": "00bebcfc",
  "target": "00bebdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd00`](#insn-00bebd00)

~~~json
{
  "source": "00bebd00",
  "target": "00bebe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd08`](#insn-00bebd08)

~~~json
{
  "source": "00bebd08",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd1c`](#insn-00bebd1c)

~~~json
{
  "source": "00bebd1c",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd24`](#insn-00bebd24)

~~~json
{
  "source": "00bebd24",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd2c`](#insn-00bebd2c)

~~~json
{
  "source": "00bebd2c",
  "target": "00bebd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd44`](#insn-00bebd44)

~~~json
{
  "source": "00bebd44",
  "target": "00bebd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd58`](#insn-00bebd58)

~~~json
{
  "source": "00bebd58",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd64`](#insn-00bebd64)

~~~json
{
  "source": "00bebd64",
  "target": "00bebd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd78`](#insn-00bebd78)

~~~json
{
  "source": "00bebd78",
  "target": "00bebe74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebd90`](#insn-00bebd90)

~~~json
{
  "source": "00bebd90",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebda0`](#insn-00bebda0)

~~~json
{
  "source": "00bebda0",
  "target": "00bebd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdb0`](#insn-00bebdb0)

~~~json
{
  "source": "00bebdb0",
  "target": "00bebd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdc4`](#insn-00bebdc4)

~~~json
{
  "source": "00bebdc4",
  "target": "00bebda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdcc`](#insn-00bebdcc)

~~~json
{
  "source": "00bebdcc",
  "target": "00bebd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdd4`](#insn-00bebdd4)

~~~json
{
  "source": "00bebdd4",
  "target": "00bebe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdf0`](#insn-00bebdf0)

~~~json
{
  "source": "00bebdf0",
  "target": "00bebe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe00`](#insn-00bebe00)

~~~json
{
  "source": "00bebe00",
  "target": "00bebe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe10`](#insn-00bebe10)

~~~json
{
  "source": "00bebe10",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe28`](#insn-00bebe28)

~~~json
{
  "source": "00bebe28",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe38`](#insn-00bebe38)

~~~json
{
  "source": "00bebe38",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe40`](#insn-00bebe40)

~~~json
{
  "source": "00bebe40",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe50`](#insn-00bebe50)

~~~json
{
  "source": "00bebe50",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe60`](#insn-00bebe60)

~~~json
{
  "source": "00bebe60",
  "target": "00bebe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe68`](#insn-00bebe68)

~~~json
{
  "source": "00bebe68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe80`](#insn-00bebe80)

~~~json
{
  "source": "00bebe80",
  "target": "00bebe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
