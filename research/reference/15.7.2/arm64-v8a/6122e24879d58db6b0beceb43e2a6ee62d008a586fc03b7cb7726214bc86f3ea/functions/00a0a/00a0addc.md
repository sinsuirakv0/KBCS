# 00a0addc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0addc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0addc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0039.md#compare-251d4a6a5957428a5832709d9c4e91f2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0addc",
  "name": "FUN_00a0addc",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45c44d40e76d6c2e6a71388718e787e112b802f96d17071a5193f84e92d50935",
  "source_text_sha256": "45c44d40e76d6c2e6a71388718e787e112b802f96d17071a5193f84e92d50935",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0addc",
        "00a0b03b"
      ]
    ],
    "bytes_sha256": "eef158bd0ec3f7c48e4c4961e10c46476a25dddda72507028d96162b6357668b",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a0bbd8](../00a0b/00a0bbd8.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041fdf0](../0041f/0041fdf0.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4655 bytes

~~~c

void FUN_00a0addc(long param_1,int param_2,int param_3,int param_4)

{
  int iVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  
  puVar7 = (undefined8 *)(param_1 + 0x10);
  puVar3 = (undefined8 *)*puVar7;
  puVar6 = puVar3;
  puVar5 = puVar7;
  if (puVar3 != (undefined8 *)0x0) {
    do {
      iVar1 = param_4;
      if (*(int *)(puVar6 + 4) <= param_2) {
        puVar5 = puVar3;
        if (param_2 <= *(int *)(puVar6 + 4)) goto LAB_00a0ae50;
        puVar6 = puVar6 + 1;
      }
      puVar6 = (undefined8 *)*puVar6;
    } while (puVar6 != (undefined8 *)0x0);
LAB_00a0af10:
    do {
      param_4 = iVar1;
      puVar7 = puVar3;
      iVar1 = param_4;
      if (*(int *)(puVar7 + 4) <= param_2) {
        puVar6 = puVar7;
        if (param_2 <= *(int *)(puVar7 + 4)) goto LAB_00a0af94;
        puVar3 = (undefined8 *)puVar7[1];
        if ((undefined8 *)puVar7[1] == (undefined8 *)0x0) {
          puVar5 = puVar7 + 1;
          break;
        }
        goto LAB_00a0af10;
      }
      puVar3 = (undefined8 *)*puVar7;
      puVar5 = puVar7;
    } while ((undefined8 *)*puVar7 != (undefined8 *)0x0);
  }
  puVar6 = (undefined8 *)_Znwm(0x40);
  puVar6[7] = 0;
  puVar6[6] = 0;
  puVar6[5] = puVar6 + 6;
  *puVar6 = 0;
  puVar6[1] = 0;
  puVar6[2] = puVar7;
  *puVar5 = puVar6;
                    /* try { // try from 00a0af68 to 00b0af73 has its CatchHandler @ 00a0d0f4 */
  plVar4 = *(long **)(param_1 + 8);
  *(int *)(puVar6 + 4) = param_2;
  puVar3 = puVar6;
  if (*plVar4 != 0) {
    *(long *)(param_1 + 8) = *plVar4;
    puVar3 = (undefined8 *)*puVar5;
  }
  FUN_00419064(*(undefined8 *)(param_1 + 0x10),puVar3);
  *(long *)(param_1 + 0x18) = *(long *)(param_1 + 0x18) + 1;
LAB_00a0af94:
  puVar5 = (undefined8 *)puVar6[6];
  puVar3 = puVar6 + 6;
  do {
    puVar7 = puVar3;
    if (puVar5 == (undefined8 *)0x0) {
LAB_00a0afd4:
      puVar2 = (undefined8 *)_Znwm(0x28);
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar3;
      *puVar7 = puVar2;
      plVar4 = (long *)puVar6[5];
      *(int *)((long)puVar2 + 0x1c) = param_3;
      *(undefined4 *)(puVar2 + 4) = 0;
      puVar3 = puVar2;
      if (*plVar4 != 0) {
        puVar6[5] = *plVar4;
        puVar3 = (undefined8 *)*puVar7;
      }
      FUN_00419064(puVar6[6],puVar3);
      puVar6[7] = puVar6[7] + 1;
LAB_00a0b020:
      *(int *)(puVar2 + 4) = param_4;
                    /* try { // try from 00a0b030 to 00b0b03b has its CatchHandler @ 00a0d26c */
      return;
    }
    while (puVar2 = puVar5, puVar3 = puVar2, *(int *)((long)puVar2 + 0x1c) <= param_3) {
      if (param_3 <= *(int *)((long)puVar2 + 0x1c)) goto LAB_00a0b020;
      puVar5 = (undefined8 *)puVar2[1];
      if ((undefined8 *)puVar2[1] == (undefined8 *)0x0) {
        puVar7 = puVar2 + 1;
        goto LAB_00a0afd4;
      }
    }
    puVar5 = (undefined8 *)*puVar2;
  } while( true );
  while (puVar5 != (undefined8 *)0x0) {
LAB_00a0ae50:
    if (param_2 < *(int *)(puVar5 + 4)) {
      puVar5 = (undefined8 *)*puVar5;
    }
    else {
      if (param_2 <= *(int *)(puVar5 + 4)) {
        plVar4 = (long *)puVar5[6];
        goto joined_r0x00a0ae78;
      }
      puVar5 = (undefined8 *)puVar5[1];
    }
  }
  goto LAB_00a0ae68;
joined_r0x00a0ae78:
  if (plVar4 == (long *)0x0) goto LAB_00a0af10;
  if (*(int *)((long)plVar4 + 0x1c) <= param_3) {
    puVar6 = puVar3;
    if (param_3 <= *(int *)((long)plVar4 + 0x1c)) goto LAB_00a0aeac;
    plVar4 = plVar4 + 1;
  }
  plVar4 = (long *)*plVar4;
  goto joined_r0x00a0ae78;
  while (puVar6 != (undefined8 *)0x0) {
LAB_00a0aeac:
    if (param_2 < *(int *)(puVar6 + 4)) {
      puVar6 = (undefined8 *)*puVar6;
    }
    else {
      if (param_2 <= *(int *)(puVar6 + 4)) {
        plVar4 = (long *)puVar6[6];
        goto joined_r0x00a0aecc;
      }
                    /* try { // try from 00a0aebc to 00b0aec7 has its CatchHandler @ 00a0d11c */
      puVar6 = (undefined8 *)puVar6[1];
    }
  }
  goto LAB_00a0ae68;
joined_r0x00a0aecc:
  if (plVar4 != (long *)0x0) {
    if (param_3 < *(int *)((long)plVar4 + 0x1c)) {
      plVar4 = (long *)*plVar4;
    }
    else {
      if (param_3 <= *(int *)((long)plVar4 + 0x1c)) {
        iVar1 = *(int *)(plVar4 + 4);
        if (*(int *)(plVar4 + 4) <= param_4) {
          iVar1 = param_4;
        }
        goto LAB_00a0af10;
      }
                    /* try { // try from 00a0aeec to 00b0aef7 has its CatchHandler @ 00a0d118 */
      plVar4 = (long *)plVar4[1];
    }
    goto joined_r0x00a0aecc;
  }
LAB_00a0ae68:
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a0addc"></a> `00a0addc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a0ade0"></a> `00a0ade0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ade4"></a> `00a0ade4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ade8"></a> `00a0ade8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0adec"></a> `00a0adec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a0adf0"></a> `00a0adf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a0adf4"></a> `00a0adf4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00a0adf8"></a> `00a0adf8` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00a0adfc"></a> `00a0adfc` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00a0ae00"></a> `00a0ae00` | `08 0f 41 f8` | ldr x8,[x24, #0x10]! | `FALL_THROUGH`
<a id="insn-00a0ae04"></a> `00a0ae04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00a0ae08"></a> `00a0ae08` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-00a0ae0c"></a> `00a0ae0c` | `68 01 00 b4` | cbz x8,0x00a0ae38 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae10"></a> `00a0ae10` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a0ae14"></a> `00a0ae14` | `03 00 00 14` | b 0x00a0ae20 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ae18"></a> `00a0ae18` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0ae1c"></a> `00a0ae1c` | `a9 07 00 b4` | cbz x9,0x00a0af10 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae20"></a> `00a0ae20` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ae24"></a> `00a0ae24` | `5f 01 16 6b` | cmp w10,w22 | `FALL_THROUGH`
<a id="insn-00a0ae28"></a> `00a0ae28` | `8c ff ff 54` | b.gt 0x00a0ae18 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae2c"></a> `00a0ae2c` | `aa 00 00 54` | b.ge 0x00a0ae40 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae30"></a> `00a0ae30` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ae34"></a> `00a0ae34` | `f9 ff ff 17` | b 0x00a0ae18 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ae38"></a> `00a0ae38` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00a0ae3c"></a> `00a0ae3c` | `3f 00 00 14` | b 0x00a0af38 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ae40"></a> `00a0ae40` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a0ae44"></a> `00a0ae44` | `03 00 00 14` | b 0x00a0ae50 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ae48"></a> `00a0ae48` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0ae4c"></a> `00a0ae4c` | `e9 00 00 b4` | cbz x9,0x00a0ae68 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae50"></a> `00a0ae50` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ae54"></a> `00a0ae54` | `5f 01 16 6b` | cmp w10,w22 | `FALL_THROUGH`
<a id="insn-00a0ae58"></a> `00a0ae58` | `8c ff ff 54` | b.gt 0x00a0ae48 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae5c"></a> `00a0ae5c` | `ca 00 00 54` | b.ge 0x00a0ae74 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae60"></a> `00a0ae60` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ae64"></a> `00a0ae64` | `69 ff ff b5` | cbnz x9,0x00a0ae50 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae68"></a> `00a0ae68` | `20 c4 ff d0` | adrp x0,0x290000 | `FALL_THROUGH`
<a id="insn-00a0ae6c"></a> `00a0ae6c` | `00 b8 2e 91` | add x0,x0,#0xbae | `FALL_THROUGH`
<a id="insn-00a0ae70"></a> `00a0ae70` | `e0 53 e8 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-00a0ae74"></a> `00a0ae74` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ae78"></a> `00a0ae78` | `a9 00 00 b5` | cbnz x9,0x00a0ae8c | `CONDITIONAL_JUMP`
<a id="insn-00a0ae7c"></a> `00a0ae7c` | `25 00 00 14` | b 0x00a0af10 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ae80"></a> `00a0ae80` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ae84"></a> `00a0ae84` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0ae88"></a> `00a0ae88` | `49 04 00 b4` | cbz x9,0x00a0af10 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae8c"></a> `00a0ae8c` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0ae90"></a> `00a0ae90` | `5f 01 14 6b` | cmp w10,w20 | `FALL_THROUGH`
<a id="insn-00a0ae94"></a> `00a0ae94` | `8c ff ff 54` | b.gt 0x00a0ae84 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae98"></a> `00a0ae98` | `4b ff ff 54` | b.lt 0x00a0ae80 | `CONDITIONAL_JUMP`
<a id="insn-00a0ae9c"></a> `00a0ae9c` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a0aea0"></a> `00a0aea0` | `03 00 00 14` | b 0x00a0aeac | `UNCONDITIONAL_JUMP`
<a id="insn-00a0aea4"></a> `00a0aea4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0aea8"></a> `00a0aea8` | `09 fe ff b4` | cbz x9,0x00a0ae68 | `CONDITIONAL_JUMP`
<a id="insn-00a0aeac"></a> `00a0aeac` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0aeb0"></a> `00a0aeb0` | `5f 01 16 6b` | cmp w10,w22 | `FALL_THROUGH`
<a id="insn-00a0aeb4"></a> `00a0aeb4` | `8c ff ff 54` | b.gt 0x00a0aea4 | `CONDITIONAL_JUMP`
<a id="insn-00a0aeb8"></a> `00a0aeb8` | `8a 00 00 54` | b.ge 0x00a0aec8 | `CONDITIONAL_JUMP`
<a id="insn-00a0aebc"></a> `00a0aebc` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a0aec0"></a> `00a0aec0` | `69 ff ff b5` | cbnz x9,0x00a0aeac | `CONDITIONAL_JUMP`
<a id="insn-00a0aec4"></a> `00a0aec4` | `e9 ff ff 17` | b 0x00a0ae68 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0aec8"></a> `00a0aec8` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00a0aecc"></a> `00a0aecc` | `89 00 00 b5` | cbnz x9,0x00a0aedc | `CONDITIONAL_JUMP`
<a id="insn-00a0aed0"></a> `00a0aed0` | `e6 ff ff 17` | b 0x00a0ae68 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0aed4"></a> `00a0aed4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a0aed8"></a> `00a0aed8` | `89 fc ff b4` | cbz x9,0x00a0ae68 | `CONDITIONAL_JUMP`
<a id="insn-00a0aedc"></a> `00a0aedc` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0aee0"></a> `00a0aee0` | `5f 01 14 6b` | cmp w10,w20 | `FALL_THROUGH`
<a id="insn-00a0aee4"></a> `00a0aee4` | `8c ff ff 54` | b.gt 0x00a0aed4 | `CONDITIONAL_JUMP`
<a id="insn-00a0aee8"></a> `00a0aee8` | `8a 00 00 54` | b.ge 0x00a0aef8 | `CONDITIONAL_JUMP`
<a id="insn-00a0aeec"></a> `00a0aeec` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a0aef0"></a> `00a0aef0` | `69 ff ff b5` | cbnz x9,0x00a0aedc | `CONDITIONAL_JUMP`
<a id="insn-00a0aef4"></a> `00a0aef4` | `dd ff ff 17` | b 0x00a0ae68 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0aef8"></a> `00a0aef8` | `29 21 40 b9` | ldr w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00a0aefc"></a> `00a0aefc` | `3f 01 13 6b` | cmp w9,w19 | `FALL_THROUGH`
<a id="insn-00a0af00"></a> `00a0af00` | `33 c1 93 1a` | csel w19,w9,w19,gt | `FALL_THROUGH`
<a id="insn-00a0af04"></a> `00a0af04` | `03 00 00 14` | b 0x00a0af10 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0af08"></a> `00a0af08` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a0af0c"></a> `00a0af0c` | `48 01 00 b4` | cbz x8,0x00a0af34 | `CONDITIONAL_JUMP`
<a id="insn-00a0af10"></a> `00a0af10` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a0af14"></a> `00a0af14` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a0af18"></a> `00a0af18` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00a0af1c"></a> `00a0af1c` | `6c ff ff 54` | b.gt 0x00a0af08 | `CONDITIONAL_JUMP`
<a id="insn-00a0af20"></a> `00a0af20` | `aa 03 00 54` | b.ge 0x00a0af94 | `CONDITIONAL_JUMP`
<a id="insn-00a0af24"></a> `00a0af24` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a0af28"></a> `00a0af28` | `48 ff ff b5` | cbnz x8,0x00a0af10 | `CONDITIONAL_JUMP`
<a id="insn-00a0af2c"></a> `00a0af2c` | `f8 22 00 91` | add x24,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a0af30"></a> `00a0af30` | `02 00 00 14` | b 0x00a0af38 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0af34"></a> `00a0af34` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00a0af38"></a> `00a0af38` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00a0af3c"></a> `00a0af3c` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00a0af40"></a> `00a0af40` | `00 40 07 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00a0af44"></a> `00a0af44` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00a0af48"></a> `00a0af48` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00a0af4c"></a> `00a0af4c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00a0af50"></a> `00a0af50` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00a0af54"></a> `00a0af54` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a0af58"></a> `00a0af58` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a0af5c"></a> `00a0af5c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a0af60"></a> `00a0af60` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a0af64"></a> `00a0af64` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00a0af68"></a> `00a0af68` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a0af6c"></a> `00a0af6c` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00a0af70"></a> `00a0af70` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0af74"></a> `00a0af74` | `68 00 00 b4` | cbz x8,0x00a0af80 | `CONDITIONAL_JUMP`
<a id="insn-00a0af78"></a> `00a0af78` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a0af7c"></a> `00a0af7c` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00a0af80"></a> `00a0af80` | `a0 0a 40 f9` | ldr x0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00a0af84"></a> `00a0af84` | `38 38 e8 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00a0af88"></a> `00a0af88` | `a8 0e 40 f9` | ldr x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00a0af8c"></a> `00a0af8c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a0af90"></a> `00a0af90` | `a8 0e 00 f9` | str x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00a0af94"></a> `00a0af94` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00a0af98"></a> `00a0af98` | `c8 0e 43 f8` | ldr x8,[x22, #0x30]! | `FALL_THROUGH`
<a id="insn-00a0af9c"></a> `00a0af9c` | `c8 00 00 b5` | cbnz x8,0x00a0afb4 | `CONDITIONAL_JUMP`
<a id="insn-00a0afa0"></a> `00a0afa0` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00a0afa4"></a> `00a0afa4` | `0c 00 00 14` | b 0x00a0afd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0afa8"></a> `00a0afa8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a0afac"></a> `00a0afac` | `f6 03 15 aa` | mov x22,x21 | `FALL_THROUGH`
<a id="insn-00a0afb0"></a> `00a0afb0` | `28 01 00 b4` | cbz x8,0x00a0afd4 | `CONDITIONAL_JUMP`
<a id="insn-00a0afb4"></a> `00a0afb4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00a0afb8"></a> `00a0afb8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0afbc"></a> `00a0afbc` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00a0afc0"></a> `00a0afc0` | `4c ff ff 54` | b.gt 0x00a0afa8 | `CONDITIONAL_JUMP`
<a id="insn-00a0afc4"></a> `00a0afc4` | `ea 02 00 54` | b.ge 0x00a0b020 | `CONDITIONAL_JUMP`
<a id="insn-00a0afc8"></a> `00a0afc8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a0afcc"></a> `00a0afcc` | `48 ff ff b5` | cbnz x8,0x00a0afb4 | `CONDITIONAL_JUMP`
<a id="insn-00a0afd0"></a> `00a0afd0` | `b6 22 00 91` | add x22,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a0afd4"></a> `00a0afd4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00a0afd8"></a> `00a0afd8` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00a0afdc"></a> `00a0afdc` | `d9 3f 07 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00a0afe0"></a> `00a0afe0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a0afe4"></a> `00a0afe4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00a0afe8"></a> `00a0afe8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a0afec"></a> `00a0afec` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a0aff0"></a> `00a0aff0` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00a0aff4"></a> `00a0aff4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00a0aff8"></a> `00a0aff8` | `14 fc 03 29` | stp w20,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0affc"></a> `00a0affc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0b000"></a> `00a0b000` | `68 00 00 b4` | cbz x8,0x00a0b00c | `CONDITIONAL_JUMP`
<a id="insn-00a0b004"></a> `00a0b004` | `e8 16 00 f9` | str x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00a0b008"></a> `00a0b008` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00a0b00c"></a> `00a0b00c` | `e0 1a 40 f9` | ldr x0,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00a0b010"></a> `00a0b010` | `15 38 e8 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00a0b014"></a> `00a0b014` | `e8 1e 40 f9` | ldr x8,[x23, #0x38] | `FALL_THROUGH`
<a id="insn-00a0b018"></a> `00a0b018` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a0b01c"></a> `00a0b01c` | `e8 1e 00 f9` | str x8,[x23, #0x38] | `FALL_THROUGH`
<a id="insn-00a0b020"></a> `00a0b020` | `b3 22 00 b9` | str w19,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00a0b024"></a> `00a0b024` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a0b028"></a> `00a0b028` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0b02c"></a> `00a0b02c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0b030"></a> `00a0b030` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0b034"></a> `00a0b034` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a0b038"></a> `00a0b038` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0addc`](#insn-00a0addc) 範囲 `[['00a0addc', '00a0ae0f']]`
  - `CONDITIONAL_JUMP` [`00a0ae0c`](#insn-00a0ae0c) → [`00a0ae38`](#insn-00a0ae38)
  - `FALL_THROUGH` [`00a0ae0c`](#insn-00a0ae0c) → [`00a0ae10`](#insn-00a0ae10)
- ブロック [`00a0ae10`](#insn-00a0ae10) 範囲 `[['00a0ae10', '00a0ae17']]`
  - `UNCONDITIONAL_JUMP` [`00a0ae14`](#insn-00a0ae14) → [`00a0ae20`](#insn-00a0ae20)
- ブロック [`00a0ae18`](#insn-00a0ae18) 範囲 `[['00a0ae18', '00a0ae1f']]`
  - `CONDITIONAL_JUMP` [`00a0ae1c`](#insn-00a0ae1c) → [`00a0af10`](#insn-00a0af10)
  - `FALL_THROUGH` [`00a0ae1c`](#insn-00a0ae1c) → [`00a0ae20`](#insn-00a0ae20)
- ブロック [`00a0ae20`](#insn-00a0ae20) 範囲 `[['00a0ae20', '00a0ae2b']]`
  - `CONDITIONAL_JUMP` [`00a0ae28`](#insn-00a0ae28) → [`00a0ae18`](#insn-00a0ae18)
  - `FALL_THROUGH` [`00a0ae28`](#insn-00a0ae28) → [`00a0ae2c`](#insn-00a0ae2c)
- ブロック [`00a0ae2c`](#insn-00a0ae2c) 範囲 `[['00a0ae2c', '00a0ae2f']]`
  - `CONDITIONAL_JUMP` [`00a0ae2c`](#insn-00a0ae2c) → [`00a0ae40`](#insn-00a0ae40)
  - `FALL_THROUGH` [`00a0ae2c`](#insn-00a0ae2c) → [`00a0ae30`](#insn-00a0ae30)
- ブロック [`00a0ae30`](#insn-00a0ae30) 範囲 `[['00a0ae30', '00a0ae37']]`
  - `UNCONDITIONAL_JUMP` [`00a0ae34`](#insn-00a0ae34) → [`00a0ae18`](#insn-00a0ae18)
- ブロック [`00a0ae38`](#insn-00a0ae38) 範囲 `[['00a0ae38', '00a0ae3f']]`
  - `UNCONDITIONAL_JUMP` [`00a0ae3c`](#insn-00a0ae3c) → [`00a0af38`](#insn-00a0af38)
- ブロック [`00a0ae40`](#insn-00a0ae40) 範囲 `[['00a0ae40', '00a0ae47']]`
  - `UNCONDITIONAL_JUMP` [`00a0ae44`](#insn-00a0ae44) → [`00a0ae50`](#insn-00a0ae50)
- ブロック [`00a0ae48`](#insn-00a0ae48) 範囲 `[['00a0ae48', '00a0ae4f']]`
  - `CONDITIONAL_JUMP` [`00a0ae4c`](#insn-00a0ae4c) → [`00a0ae68`](#insn-00a0ae68)
  - `FALL_THROUGH` [`00a0ae4c`](#insn-00a0ae4c) → [`00a0ae50`](#insn-00a0ae50)
- ブロック [`00a0ae50`](#insn-00a0ae50) 範囲 `[['00a0ae50', '00a0ae5b']]`
  - `CONDITIONAL_JUMP` [`00a0ae58`](#insn-00a0ae58) → [`00a0ae48`](#insn-00a0ae48)
  - `FALL_THROUGH` [`00a0ae58`](#insn-00a0ae58) → [`00a0ae5c`](#insn-00a0ae5c)
- ブロック [`00a0ae5c`](#insn-00a0ae5c) 範囲 `[['00a0ae5c', '00a0ae5f']]`
  - `CONDITIONAL_JUMP` [`00a0ae5c`](#insn-00a0ae5c) → [`00a0ae74`](#insn-00a0ae74)
  - `FALL_THROUGH` [`00a0ae5c`](#insn-00a0ae5c) → [`00a0ae60`](#insn-00a0ae60)
- ブロック [`00a0ae60`](#insn-00a0ae60) 範囲 `[['00a0ae60', '00a0ae67']]`
  - `CONDITIONAL_JUMP` [`00a0ae64`](#insn-00a0ae64) → [`00a0ae50`](#insn-00a0ae50)
  - `FALL_THROUGH` [`00a0ae64`](#insn-00a0ae64) → [`00a0ae68`](#insn-00a0ae68)
- ブロック [`00a0ae68`](#insn-00a0ae68) 範囲 `[['00a0ae68', '00a0ae73']]`
- ブロック [`00a0ae74`](#insn-00a0ae74) 範囲 `[['00a0ae74', '00a0ae7b']]`
  - `CONDITIONAL_JUMP` [`00a0ae78`](#insn-00a0ae78) → [`00a0ae8c`](#insn-00a0ae8c)
  - `FALL_THROUGH` [`00a0ae78`](#insn-00a0ae78) → [`00a0ae7c`](#insn-00a0ae7c)
- ブロック [`00a0ae7c`](#insn-00a0ae7c) 範囲 `[['00a0ae7c', '00a0ae7f']]`
  - `UNCONDITIONAL_JUMP` [`00a0ae7c`](#insn-00a0ae7c) → [`00a0af10`](#insn-00a0af10)
- ブロック [`00a0ae80`](#insn-00a0ae80) 範囲 `[['00a0ae80', '00a0ae83']]`
  - `FALL_THROUGH` [`00a0ae80`](#insn-00a0ae80) → [`00a0ae84`](#insn-00a0ae84)
- ブロック [`00a0ae84`](#insn-00a0ae84) 範囲 `[['00a0ae84', '00a0ae8b']]`
  - `CONDITIONAL_JUMP` [`00a0ae88`](#insn-00a0ae88) → [`00a0af10`](#insn-00a0af10)
  - `FALL_THROUGH` [`00a0ae88`](#insn-00a0ae88) → [`00a0ae8c`](#insn-00a0ae8c)
- ブロック [`00a0ae8c`](#insn-00a0ae8c) 範囲 `[['00a0ae8c', '00a0ae97']]`
  - `CONDITIONAL_JUMP` [`00a0ae94`](#insn-00a0ae94) → [`00a0ae84`](#insn-00a0ae84)
  - `FALL_THROUGH` [`00a0ae94`](#insn-00a0ae94) → [`00a0ae98`](#insn-00a0ae98)
- ブロック [`00a0ae98`](#insn-00a0ae98) 範囲 `[['00a0ae98', '00a0ae9b']]`
  - `CONDITIONAL_JUMP` [`00a0ae98`](#insn-00a0ae98) → [`00a0ae80`](#insn-00a0ae80)
  - `FALL_THROUGH` [`00a0ae98`](#insn-00a0ae98) → [`00a0ae9c`](#insn-00a0ae9c)
- ブロック [`00a0ae9c`](#insn-00a0ae9c) 範囲 `[['00a0ae9c', '00a0aea3']]`
  - `UNCONDITIONAL_JUMP` [`00a0aea0`](#insn-00a0aea0) → [`00a0aeac`](#insn-00a0aeac)
- ブロック [`00a0aea4`](#insn-00a0aea4) 範囲 `[['00a0aea4', '00a0aeab']]`
  - `CONDITIONAL_JUMP` [`00a0aea8`](#insn-00a0aea8) → [`00a0ae68`](#insn-00a0ae68)
  - `FALL_THROUGH` [`00a0aea8`](#insn-00a0aea8) → [`00a0aeac`](#insn-00a0aeac)
- ブロック [`00a0aeac`](#insn-00a0aeac) 範囲 `[['00a0aeac', '00a0aeb7']]`
  - `CONDITIONAL_JUMP` [`00a0aeb4`](#insn-00a0aeb4) → [`00a0aea4`](#insn-00a0aea4)
  - `FALL_THROUGH` [`00a0aeb4`](#insn-00a0aeb4) → [`00a0aeb8`](#insn-00a0aeb8)
- ブロック [`00a0aeb8`](#insn-00a0aeb8) 範囲 `[['00a0aeb8', '00a0aebb']]`
  - `CONDITIONAL_JUMP` [`00a0aeb8`](#insn-00a0aeb8) → [`00a0aec8`](#insn-00a0aec8)
  - `FALL_THROUGH` [`00a0aeb8`](#insn-00a0aeb8) → [`00a0aebc`](#insn-00a0aebc)
- ブロック [`00a0aebc`](#insn-00a0aebc) 範囲 `[['00a0aebc', '00a0aec3']]`
  - `CONDITIONAL_JUMP` [`00a0aec0`](#insn-00a0aec0) → [`00a0aeac`](#insn-00a0aeac)
  - `FALL_THROUGH` [`00a0aec0`](#insn-00a0aec0) → [`00a0aec4`](#insn-00a0aec4)
- ブロック [`00a0aec4`](#insn-00a0aec4) 範囲 `[['00a0aec4', '00a0aec7']]`
  - `UNCONDITIONAL_JUMP` [`00a0aec4`](#insn-00a0aec4) → [`00a0ae68`](#insn-00a0ae68)
- ブロック [`00a0aec8`](#insn-00a0aec8) 範囲 `[['00a0aec8', '00a0aecf']]`
  - `CONDITIONAL_JUMP` [`00a0aecc`](#insn-00a0aecc) → [`00a0aedc`](#insn-00a0aedc)
  - `FALL_THROUGH` [`00a0aecc`](#insn-00a0aecc) → [`00a0aed0`](#insn-00a0aed0)
- ブロック [`00a0aed0`](#insn-00a0aed0) 範囲 `[['00a0aed0', '00a0aed3']]`
  - `UNCONDITIONAL_JUMP` [`00a0aed0`](#insn-00a0aed0) → [`00a0ae68`](#insn-00a0ae68)
- ブロック [`00a0aed4`](#insn-00a0aed4) 範囲 `[['00a0aed4', '00a0aedb']]`
  - `CONDITIONAL_JUMP` [`00a0aed8`](#insn-00a0aed8) → [`00a0ae68`](#insn-00a0ae68)
  - `FALL_THROUGH` [`00a0aed8`](#insn-00a0aed8) → [`00a0aedc`](#insn-00a0aedc)
- ブロック [`00a0aedc`](#insn-00a0aedc) 範囲 `[['00a0aedc', '00a0aee7']]`
  - `CONDITIONAL_JUMP` [`00a0aee4`](#insn-00a0aee4) → [`00a0aed4`](#insn-00a0aed4)
  - `FALL_THROUGH` [`00a0aee4`](#insn-00a0aee4) → [`00a0aee8`](#insn-00a0aee8)
- ブロック [`00a0aee8`](#insn-00a0aee8) 範囲 `[['00a0aee8', '00a0aeeb']]`
  - `CONDITIONAL_JUMP` [`00a0aee8`](#insn-00a0aee8) → [`00a0aef8`](#insn-00a0aef8)
  - `FALL_THROUGH` [`00a0aee8`](#insn-00a0aee8) → [`00a0aeec`](#insn-00a0aeec)
- ブロック [`00a0aeec`](#insn-00a0aeec) 範囲 `[['00a0aeec', '00a0aef3']]`
  - `CONDITIONAL_JUMP` [`00a0aef0`](#insn-00a0aef0) → [`00a0aedc`](#insn-00a0aedc)
  - `FALL_THROUGH` [`00a0aef0`](#insn-00a0aef0) → [`00a0aef4`](#insn-00a0aef4)
- ブロック [`00a0aef4`](#insn-00a0aef4) 範囲 `[['00a0aef4', '00a0aef7']]`
  - `UNCONDITIONAL_JUMP` [`00a0aef4`](#insn-00a0aef4) → [`00a0ae68`](#insn-00a0ae68)
- ブロック [`00a0aef8`](#insn-00a0aef8) 範囲 `[['00a0aef8', '00a0af07']]`
  - `UNCONDITIONAL_JUMP` [`00a0af04`](#insn-00a0af04) → [`00a0af10`](#insn-00a0af10)
- ブロック [`00a0af08`](#insn-00a0af08) 範囲 `[['00a0af08', '00a0af0f']]`
  - `CONDITIONAL_JUMP` [`00a0af0c`](#insn-00a0af0c) → [`00a0af34`](#insn-00a0af34)
  - `FALL_THROUGH` [`00a0af0c`](#insn-00a0af0c) → [`00a0af10`](#insn-00a0af10)
- ブロック [`00a0af10`](#insn-00a0af10) 範囲 `[['00a0af10', '00a0af1f']]`
  - `CONDITIONAL_JUMP` [`00a0af1c`](#insn-00a0af1c) → [`00a0af08`](#insn-00a0af08)
  - `FALL_THROUGH` [`00a0af1c`](#insn-00a0af1c) → [`00a0af20`](#insn-00a0af20)
- ブロック [`00a0af20`](#insn-00a0af20) 範囲 `[['00a0af20', '00a0af23']]`
  - `CONDITIONAL_JUMP` [`00a0af20`](#insn-00a0af20) → [`00a0af94`](#insn-00a0af94)
  - `FALL_THROUGH` [`00a0af20`](#insn-00a0af20) → [`00a0af24`](#insn-00a0af24)
- ブロック [`00a0af24`](#insn-00a0af24) 範囲 `[['00a0af24', '00a0af2b']]`
  - `CONDITIONAL_JUMP` [`00a0af28`](#insn-00a0af28) → [`00a0af10`](#insn-00a0af10)
  - `FALL_THROUGH` [`00a0af28`](#insn-00a0af28) → [`00a0af2c`](#insn-00a0af2c)
- ブロック [`00a0af2c`](#insn-00a0af2c) 範囲 `[['00a0af2c', '00a0af33']]`
  - `UNCONDITIONAL_JUMP` [`00a0af30`](#insn-00a0af30) → [`00a0af38`](#insn-00a0af38)
- ブロック [`00a0af34`](#insn-00a0af34) 範囲 `[['00a0af34', '00a0af37']]`
  - `FALL_THROUGH` [`00a0af34`](#insn-00a0af34) → [`00a0af38`](#insn-00a0af38)
- ブロック [`00a0af38`](#insn-00a0af38) 範囲 `[['00a0af38', '00a0af67']]`
  - `FALL_THROUGH` [`00a0af64`](#insn-00a0af64) → [`00a0af68`](#insn-00a0af68)
- ブロック [`00a0af68`](#insn-00a0af68) 範囲 `[['00a0af68', '00a0af77']]`
  - `CONDITIONAL_JUMP` [`00a0af74`](#insn-00a0af74) → [`00a0af80`](#insn-00a0af80)
  - `FALL_THROUGH` [`00a0af74`](#insn-00a0af74) → [`00a0af78`](#insn-00a0af78)
- ブロック [`00a0af78`](#insn-00a0af78) 範囲 `[['00a0af78', '00a0af7f']]`
  - `FALL_THROUGH` [`00a0af7c`](#insn-00a0af7c) → [`00a0af80`](#insn-00a0af80)
- ブロック [`00a0af80`](#insn-00a0af80) 範囲 `[['00a0af80', '00a0af93']]`
  - `FALL_THROUGH` [`00a0af90`](#insn-00a0af90) → [`00a0af94`](#insn-00a0af94)
- ブロック [`00a0af94`](#insn-00a0af94) 範囲 `[['00a0af94', '00a0af9f']]`
  - `CONDITIONAL_JUMP` [`00a0af9c`](#insn-00a0af9c) → [`00a0afb4`](#insn-00a0afb4)
  - `FALL_THROUGH` [`00a0af9c`](#insn-00a0af9c) → [`00a0afa0`](#insn-00a0afa0)
- ブロック [`00a0afa0`](#insn-00a0afa0) 範囲 `[['00a0afa0', '00a0afa7']]`
  - `UNCONDITIONAL_JUMP` [`00a0afa4`](#insn-00a0afa4) → [`00a0afd4`](#insn-00a0afd4)
- ブロック [`00a0afa8`](#insn-00a0afa8) 範囲 `[['00a0afa8', '00a0afb3']]`
  - `CONDITIONAL_JUMP` [`00a0afb0`](#insn-00a0afb0) → [`00a0afd4`](#insn-00a0afd4)
  - `FALL_THROUGH` [`00a0afb0`](#insn-00a0afb0) → [`00a0afb4`](#insn-00a0afb4)
- ブロック [`00a0afb4`](#insn-00a0afb4) 範囲 `[['00a0afb4', '00a0afc3']]`
  - `CONDITIONAL_JUMP` [`00a0afc0`](#insn-00a0afc0) → [`00a0afa8`](#insn-00a0afa8)
  - `FALL_THROUGH` [`00a0afc0`](#insn-00a0afc0) → [`00a0afc4`](#insn-00a0afc4)
- ブロック [`00a0afc4`](#insn-00a0afc4) 範囲 `[['00a0afc4', '00a0afc7']]`
  - `CONDITIONAL_JUMP` [`00a0afc4`](#insn-00a0afc4) → [`00a0b020`](#insn-00a0b020)
  - `FALL_THROUGH` [`00a0afc4`](#insn-00a0afc4) → [`00a0afc8`](#insn-00a0afc8)
- ブロック [`00a0afc8`](#insn-00a0afc8) 範囲 `[['00a0afc8', '00a0afcf']]`
  - `CONDITIONAL_JUMP` [`00a0afcc`](#insn-00a0afcc) → [`00a0afb4`](#insn-00a0afb4)
  - `FALL_THROUGH` [`00a0afcc`](#insn-00a0afcc) → [`00a0afd0`](#insn-00a0afd0)
- ブロック [`00a0afd0`](#insn-00a0afd0) 範囲 `[['00a0afd0', '00a0afd3']]`
  - `FALL_THROUGH` [`00a0afd0`](#insn-00a0afd0) → [`00a0afd4`](#insn-00a0afd4)
- ブロック [`00a0afd4`](#insn-00a0afd4) 範囲 `[['00a0afd4', '00a0b003']]`
  - `CONDITIONAL_JUMP` [`00a0b000`](#insn-00a0b000) → [`00a0b00c`](#insn-00a0b00c)
  - `FALL_THROUGH` [`00a0b000`](#insn-00a0b000) → [`00a0b004`](#insn-00a0b004)
- ブロック [`00a0b004`](#insn-00a0b004) 範囲 `[['00a0b004', '00a0b00b']]`
  - `FALL_THROUGH` [`00a0b008`](#insn-00a0b008) → [`00a0b00c`](#insn-00a0b00c)
- ブロック [`00a0b00c`](#insn-00a0b00c) 範囲 `[['00a0b00c', '00a0b01f']]`
  - `FALL_THROUGH` [`00a0b01c`](#insn-00a0b01c) → [`00a0b020`](#insn-00a0b020)
- ブロック [`00a0b020`](#insn-00a0b020) 範囲 `[['00a0b020', '00a0b02f']]`
  - `FALL_THROUGH` [`00a0b02c`](#insn-00a0b02c) → [`00a0b030`](#insn-00a0b030)
- ブロック [`00a0b030`](#insn-00a0b030) 範囲 `[['00a0b030', '00a0b03b']]`

## 命令位置別の参照

- [`00a0addc`](#insn-00a0addc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ade0`](#insn-00a0ade0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ade4`](#insn-00a0ade4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ade8`](#insn-00a0ade8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0adec`](#insn-00a0adec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae0c`](#insn-00a0ae0c) → [`00a0ae38`](#insn-00a0ae38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae14`](#insn-00a0ae14) → [`00a0ae20`](#insn-00a0ae20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae1c`](#insn-00a0ae1c) → [`00a0af10`](#insn-00a0af10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae28`](#insn-00a0ae28) → [`00a0ae18`](#insn-00a0ae18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae2c`](#insn-00a0ae2c) → [`00a0ae40`](#insn-00a0ae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae34`](#insn-00a0ae34) → [`00a0ae18`](#insn-00a0ae18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae3c`](#insn-00a0ae3c) → [`00a0af38`](#insn-00a0af38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae44`](#insn-00a0ae44) → [`00a0ae50`](#insn-00a0ae50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae4c`](#insn-00a0ae4c) → [`00a0ae68`](#insn-00a0ae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae58`](#insn-00a0ae58) → [`00a0ae48`](#insn-00a0ae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae5c`](#insn-00a0ae5c) → [`00a0ae74`](#insn-00a0ae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae64`](#insn-00a0ae64) → [`00a0ae50`](#insn-00a0ae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae6c`](#insn-00a0ae6c) → `00290bae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a0ae70`](#insn-00a0ae70) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae78`](#insn-00a0ae78) → [`00a0ae8c`](#insn-00a0ae8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae7c`](#insn-00a0ae7c) → [`00a0af10`](#insn-00a0af10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae88`](#insn-00a0ae88) → [`00a0af10`](#insn-00a0af10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae94`](#insn-00a0ae94) → [`00a0ae84`](#insn-00a0ae84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ae98`](#insn-00a0ae98) → [`00a0ae80`](#insn-00a0ae80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aea0`](#insn-00a0aea0) → [`00a0aeac`](#insn-00a0aeac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aea8`](#insn-00a0aea8) → [`00a0ae68`](#insn-00a0ae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aeb4`](#insn-00a0aeb4) → [`00a0aea4`](#insn-00a0aea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aeb8`](#insn-00a0aeb8) → [`00a0aec8`](#insn-00a0aec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aec0`](#insn-00a0aec0) → [`00a0aeac`](#insn-00a0aeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aec4`](#insn-00a0aec4) → [`00a0ae68`](#insn-00a0ae68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aecc`](#insn-00a0aecc) → [`00a0aedc`](#insn-00a0aedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aed0`](#insn-00a0aed0) → [`00a0ae68`](#insn-00a0ae68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aed8`](#insn-00a0aed8) → [`00a0ae68`](#insn-00a0ae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aee4`](#insn-00a0aee4) → [`00a0aed4`](#insn-00a0aed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aee8`](#insn-00a0aee8) → [`00a0aef8`](#insn-00a0aef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aef0`](#insn-00a0aef0) → [`00a0aedc`](#insn-00a0aedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aef4`](#insn-00a0aef4) → [`00a0ae68`](#insn-00a0ae68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af04`](#insn-00a0af04) → [`00a0af10`](#insn-00a0af10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af0c`](#insn-00a0af0c) → [`00a0af34`](#insn-00a0af34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af1c`](#insn-00a0af1c) → [`00a0af08`](#insn-00a0af08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af20`](#insn-00a0af20) → [`00a0af94`](#insn-00a0af94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af28`](#insn-00a0af28) → [`00a0af10`](#insn-00a0af10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af30`](#insn-00a0af30) → [`00a0af38`](#insn-00a0af38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af40`](#insn-00a0af40) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00a0af74`](#insn-00a0af74) → [`00a0af80`](#insn-00a0af80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0af84`](#insn-00a0af84) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00a0af9c`](#insn-00a0af9c) → [`00a0afb4`](#insn-00a0afb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afa4`](#insn-00a0afa4) → [`00a0afd4`](#insn-00a0afd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afb0`](#insn-00a0afb0) → [`00a0afd4`](#insn-00a0afd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afc0`](#insn-00a0afc0) → [`00a0afa8`](#insn-00a0afa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afc4`](#insn-00a0afc4) → [`00a0b020`](#insn-00a0b020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afcc`](#insn-00a0afcc) → [`00a0afb4`](#insn-00a0afb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0afdc`](#insn-00a0afdc) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00a0b000`](#insn-00a0b000) → [`00a0b00c`](#insn-00a0b00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0b010`](#insn-00a0b010) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00a0b024`](#insn-00a0b024) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0b028`](#insn-00a0b028) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0b02c`](#insn-00a0b02c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0b030`](#insn-00a0b030) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0b034`](#insn-00a0b034) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0addc`](#insn-00a0addc)

~~~json
{
  "source": "00a0addc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ade0`](#insn-00a0ade0)

~~~json
{
  "source": "00a0ade0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ade4`](#insn-00a0ade4)

~~~json
{
  "source": "00a0ade4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ade8`](#insn-00a0ade8)

~~~json
{
  "source": "00a0ade8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0adec`](#insn-00a0adec)

~~~json
{
  "source": "00a0adec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae0c`](#insn-00a0ae0c)

~~~json
{
  "source": "00a0ae0c",
  "target": "00a0ae38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae14`](#insn-00a0ae14)

~~~json
{
  "source": "00a0ae14",
  "target": "00a0ae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae1c`](#insn-00a0ae1c)

~~~json
{
  "source": "00a0ae1c",
  "target": "00a0af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae28`](#insn-00a0ae28)

~~~json
{
  "source": "00a0ae28",
  "target": "00a0ae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae2c`](#insn-00a0ae2c)

~~~json
{
  "source": "00a0ae2c",
  "target": "00a0ae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae34`](#insn-00a0ae34)

~~~json
{
  "source": "00a0ae34",
  "target": "00a0ae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae3c`](#insn-00a0ae3c)

~~~json
{
  "source": "00a0ae3c",
  "target": "00a0af38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae44`](#insn-00a0ae44)

~~~json
{
  "source": "00a0ae44",
  "target": "00a0ae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae4c`](#insn-00a0ae4c)

~~~json
{
  "source": "00a0ae4c",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae58`](#insn-00a0ae58)

~~~json
{
  "source": "00a0ae58",
  "target": "00a0ae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae5c`](#insn-00a0ae5c)

~~~json
{
  "source": "00a0ae5c",
  "target": "00a0ae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae64`](#insn-00a0ae64)

~~~json
{
  "source": "00a0ae64",
  "target": "00a0ae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae6c`](#insn-00a0ae6c)

~~~json
{
  "source": "00a0ae6c",
  "target": "00290bae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290bae",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "00290bae",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a0ae70`](#insn-00a0ae70)

~~~json
{
  "source": "00a0ae70",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ae78`](#insn-00a0ae78)

~~~json
{
  "source": "00a0ae78",
  "target": "00a0ae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae7c`](#insn-00a0ae7c)

~~~json
{
  "source": "00a0ae7c",
  "target": "00a0af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae88`](#insn-00a0ae88)

~~~json
{
  "source": "00a0ae88",
  "target": "00a0af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae94`](#insn-00a0ae94)

~~~json
{
  "source": "00a0ae94",
  "target": "00a0ae84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ae98`](#insn-00a0ae98)

~~~json
{
  "source": "00a0ae98",
  "target": "00a0ae80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aea0`](#insn-00a0aea0)

~~~json
{
  "source": "00a0aea0",
  "target": "00a0aeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aea8`](#insn-00a0aea8)

~~~json
{
  "source": "00a0aea8",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aeb4`](#insn-00a0aeb4)

~~~json
{
  "source": "00a0aeb4",
  "target": "00a0aea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aeb8`](#insn-00a0aeb8)

~~~json
{
  "source": "00a0aeb8",
  "target": "00a0aec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aec0`](#insn-00a0aec0)

~~~json
{
  "source": "00a0aec0",
  "target": "00a0aeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aec4`](#insn-00a0aec4)

~~~json
{
  "source": "00a0aec4",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aecc`](#insn-00a0aecc)

~~~json
{
  "source": "00a0aecc",
  "target": "00a0aedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aed0`](#insn-00a0aed0)

~~~json
{
  "source": "00a0aed0",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aed8`](#insn-00a0aed8)

~~~json
{
  "source": "00a0aed8",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aee4`](#insn-00a0aee4)

~~~json
{
  "source": "00a0aee4",
  "target": "00a0aed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aee8`](#insn-00a0aee8)

~~~json
{
  "source": "00a0aee8",
  "target": "00a0aef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aef0`](#insn-00a0aef0)

~~~json
{
  "source": "00a0aef0",
  "target": "00a0aedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aef4`](#insn-00a0aef4)

~~~json
{
  "source": "00a0aef4",
  "target": "00a0ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af04`](#insn-00a0af04)

~~~json
{
  "source": "00a0af04",
  "target": "00a0af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af0c`](#insn-00a0af0c)

~~~json
{
  "source": "00a0af0c",
  "target": "00a0af34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af1c`](#insn-00a0af1c)

~~~json
{
  "source": "00a0af1c",
  "target": "00a0af08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af20`](#insn-00a0af20)

~~~json
{
  "source": "00a0af20",
  "target": "00a0af94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af28`](#insn-00a0af28)

~~~json
{
  "source": "00a0af28",
  "target": "00a0af10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af30`](#insn-00a0af30)

~~~json
{
  "source": "00a0af30",
  "target": "00a0af38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af40`](#insn-00a0af40)

~~~json
{
  "source": "00a0af40",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0af74`](#insn-00a0af74)

~~~json
{
  "source": "00a0af74",
  "target": "00a0af80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0af84`](#insn-00a0af84)

~~~json
{
  "source": "00a0af84",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0af9c`](#insn-00a0af9c)

~~~json
{
  "source": "00a0af9c",
  "target": "00a0afb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afa4`](#insn-00a0afa4)

~~~json
{
  "source": "00a0afa4",
  "target": "00a0afd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afb0`](#insn-00a0afb0)

~~~json
{
  "source": "00a0afb0",
  "target": "00a0afd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afc0`](#insn-00a0afc0)

~~~json
{
  "source": "00a0afc0",
  "target": "00a0afa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afc4`](#insn-00a0afc4)

~~~json
{
  "source": "00a0afc4",
  "target": "00a0b020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afcc`](#insn-00a0afcc)

~~~json
{
  "source": "00a0afcc",
  "target": "00a0afb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0afdc`](#insn-00a0afdc)

~~~json
{
  "source": "00a0afdc",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0b000`](#insn-00a0b000)

~~~json
{
  "source": "00a0b000",
  "target": "00a0b00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0b010`](#insn-00a0b010)

~~~json
{
  "source": "00a0b010",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0b024`](#insn-00a0b024)

~~~json
{
  "source": "00a0b024",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0b028`](#insn-00a0b028)

~~~json
{
  "source": "00a0b028",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0b02c`](#insn-00a0b02c)

~~~json
{
  "source": "00a0b02c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0b030`](#insn-00a0b030)

~~~json
{
  "source": "00a0b030",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0b034`](#insn-00a0b034)

~~~json
{
  "source": "00a0b034",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
