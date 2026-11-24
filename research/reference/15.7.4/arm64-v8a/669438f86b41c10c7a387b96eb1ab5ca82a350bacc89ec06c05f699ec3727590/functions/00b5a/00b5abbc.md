# 00b5abbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5ab78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0069.md#compare-275b109d24bb39d2e18fe53353606924)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bca0bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-7ff749a9d06bf004a637d1896cf0ef3a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5abbc",
  "name": "_ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47cb16451d2719fdeef769598553becb2e8892acd910cb31e4b743ddd773731c",
  "source_text_sha256": "47cb16451d2719fdeef769598553becb2e8892acd910cb31e4b743ddd773731c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5abbc",
        "00b5ad9f"
      ]
    ],
    "bytes_sha256": "9528d83a4dc620ee1dbabbea043853e3159f7ff7659c5452e21697b0ec82343c",
    "instruction_count": 121,
    "instruction_bytes": 484,
    "body_bytes": 484,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bddb70](../00bdd/00bddb70.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bde2b0](../00bde/00bde2b0.md)
- [00bde760](../00bde/00bde760.md)
- [00be0990](../00be0/00be0990.md)
- [00be09d0](../00be0/00be09d0.md)
- [00be0a90](../00be0/00be0a90.md)

## 関連文字列（未確認候補）

~~~text
"Creating Auth %p for App %p"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3664 bytes

~~~c

long _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE(ulong param_1,undefined4 *param_2)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  
  puVar1 = PTR__ZN8firebase4auth13g_auths_mutexE_00c1bb70;
  uVar5 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c1bb70;
  _ZN8firebase5Mutex7AcquireEv(uVar5);
  uVar7 = *(undefined8 *)puVar1;
  _ZN8firebase5Mutex7AcquireEv(uVar7);
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c1bb78;
  puVar4 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8);
  if (puVar4 != (undefined *)0x0) {
    puVar3 = PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8;
    do {
                    /* try { // try from 00b5ac18 to 00c5ac5b has its CatchHandler @ 00b5af50 */
      if (*(ulong *)(puVar4 + 0x20) >= param_1) {
        puVar3 = puVar4;
      }
      puVar4 = *(undefined **)(puVar4 + (ulong)(*(ulong *)(puVar4 + 0x20) < param_1) * 8);
    } while (puVar4 != (undefined *)0x0);
    if ((puVar3 != PTR__ZN8firebase4auth7g_authsE_00c1bb78 + 8) &&
       (*(ulong *)(puVar3 + 0x20) <= param_1)) {
      lVar6 = *(long *)(puVar3 + 0x28);
      goto LAB_00b5ac44;
    }
  }
  lVar6 = 0;
LAB_00b5ac44:
  _ZN8firebase5Mutex7ReleaseEv(uVar7);
  if (lVar6 == 0) {
    lVar2 = _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE(param_1);
    if (lVar2 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = _Znwm(8);
      _ZN8firebase4auth4AuthC2EPNS_3AppEPv(lVar6,param_1,lVar2);
                    /* try { // try from 00b5acac to 00c5acb7 has its CatchHandler @ 00b5af24 */
      _ZN8firebase8LogDebugEPKcz("Creating Auth %p for App %p",lVar6,param_1);
      puVar10 = (undefined8 *)(puVar1 + 8);
      if ((undefined8 *)*puVar10 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = puVar10;
      }
      else {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = (undefined8 *)(puVar1 + 8);
LAB_00b5acd8:
        do {
          puVar10 = puVar8;
          if ((ulong)puVar10[4] <= param_1) {
            if ((ulong)puVar10[4] < param_1) {
              puVar9 = puVar10 + 1;
              puVar8 = (undefined8 *)*puVar9;
              if ((undefined8 *)*puVar9 != (undefined8 *)0x0) goto LAB_00b5acd8;
            }
            puVar8 = (undefined8 *)*puVar9;
            goto joined_r0x00b5ad40;
          }
          puVar8 = (undefined8 *)*puVar10;
          puVar9 = puVar10;
        } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
        puVar8 = (undefined8 *)*puVar10;
      }
joined_r0x00b5ad40:
      if (puVar8 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)_Znwm(0x30);
        puVar8[4] = param_1;
        puVar8[5] = 0;
        *puVar8 = 0;
        puVar8[1] = 0;
        puVar8[2] = puVar10;
        *puVar9 = puVar8;
        puVar10 = puVar8;
        if (**(long **)puVar1 != 0) {
          *(long *)puVar1 = **(long **)puVar1;
          puVar10 = (undefined8 *)*puVar9;
        }
        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                  (*(undefined8 *)(puVar1 + 8),puVar10);
                    /* try { // try from 00b5ad88 to 00c5ad9b has its CatchHandler @ 00b5aed0 */
        *(long *)(puVar1 + 0x10) = *(long *)(puVar1 + 0x10) + 1;
      }
      puVar8[5] = lVar6;
      if (param_2 != (undefined4 *)0x0) {
        *param_2 = 0;
      }
    }
  }
  else {
    if (param_2 != (undefined4 *)0x0) {
      *param_2 = 0;
    }
    _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE(lVar6);
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar5);
  return lVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5abbc"></a> `00b5abbc` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b5abc0"></a> `00b5abc0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5abc4"></a> `00b5abc4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5abc8"></a> `00b5abc8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5abcc"></a> `00b5abcc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5abd0"></a> `00b5abd0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b5abd4"></a> `00b5abd4` | `15 06 00 b0` | adrp x21,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b5abd8"></a> `00b5abd8` | `b5 ba 45 f9` | ldr x21,[x21, #0xb70] | `FALL_THROUGH`
<a id="insn-00b5abdc"></a> `00b5abdc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b5abe0"></a> `00b5abe0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b5abe4"></a> `00b5abe4` | `b3 02 40 f9` | ldr x19,[x21] | `FALL_THROUGH`
<a id="insn-00b5abe8"></a> `00b5abe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5abec"></a> `00b5abec` | `0d 0c 02 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5abf0"></a> `00b5abf0` | `b7 02 40 f9` | ldr x23,[x21] | `FALL_THROUGH`
<a id="insn-00b5abf4"></a> `00b5abf4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b5abf8"></a> `00b5abf8` | `0a 0c 02 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5abfc"></a> `00b5abfc` | `18 06 00 b0` | adrp x24,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b5ac00"></a> `00b5ac00` | `18 bf 45 f9` | ldr x24,[x24, #0xb78] | `FALL_THROUGH`
<a id="insn-00b5ac04"></a> `00b5ac04` | `09 07 40 f9` | ldr x9,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ac08"></a> `00b5ac08` | `c9 01 00 b4` | cbz x9,0x00b5ac40 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac0c"></a> `00b5ac0c` | `08 23 00 91` | add x8,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ac10"></a> `00b5ac10` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ac14"></a> `00b5ac14` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00b5ac18"></a> `00b5ac18` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00b5ac1c"></a> `00b5ac1c` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00b5ac20"></a> `00b5ac20` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b5ac24"></a> `00b5ac24` | `69 ff ff b5` | cbnz x9,0x00b5ac10 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac28"></a> `00b5ac28` | `09 23 00 91` | add x9,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ac2c"></a> `00b5ac2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5ac30"></a> `00b5ac30` | `80 00 00 54` | b.eq 0x00b5ac40 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac34"></a> `00b5ac34` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ac38"></a> `00b5ac38` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00b5ac3c"></a> `00b5ac3c` | `c9 06 00 54` | b.ls 0x00b5ad14 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac40"></a> `00b5ac40` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00b5ac44"></a> `00b5ac44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b5ac48"></a> `00b5ac48` | `fa 0b 02 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ac4c"></a> `00b5ac4c` | `d5 01 00 b4` | cbz x21,0x00b5ac84 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac50"></a> `00b5ac50` | `54 00 00 b4` | cbz x20,0x00b5ac58 | `CONDITIONAL_JUMP`
<a id="insn-00b5ac54"></a> `00b5ac54` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00b5ac58"></a> `00b5ac58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5ac5c"></a> `00b5ac5c` | `4d 17 02 94` | bl 0x00be0990 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ac60"></a> `00b5ac60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ac64"></a> `00b5ac64` | `f3 0b 02 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ac68"></a> `00b5ac68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5ac6c"></a> `00b5ac6c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5ac70"></a> `00b5ac70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5ac74"></a> `00b5ac74` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ac78"></a> `00b5ac78` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ac7c"></a> `00b5ac7c` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b5ac80"></a> `00b5ac80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5ac84"></a> `00b5ac84` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5ac88"></a> `00b5ac88` | `52 17 02 94` | bl 0x00be09d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ac8c"></a> `00b5ac8c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b5ac90"></a> `00b5ac90` | `60 04 00 b4` | cbz x0,0x00b5ad1c | `CONDITIONAL_JUMP`
<a id="insn-00b5ac94"></a> `00b5ac94` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00b5ac98"></a> `00b5ac98` | `ea 00 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ac9c"></a> `00b5ac9c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5aca0"></a> `00b5aca0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b5aca4"></a> `00b5aca4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00b5aca8"></a> `00b5aca8` | `7a 17 02 94` | bl 0x00be0a90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5acac"></a> `00b5acac` | `00 ba ff f0` | adrp x0,0x29d000 | `FALL_THROUGH`
<a id="insn-00b5acb0"></a> `00b5acb0` | `00 10 02 91` | add x0,x0,#0x84 | `FALL_THROUGH`
<a id="insn-00b5acb4"></a> `00b5acb4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b5acb8"></a> `00b5acb8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b5acbc"></a> `00b5acbc` | `7d 0d 02 94` | bl 0x00bde2b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5acc0"></a> `00b5acc0` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00b5acc4"></a> `00b5acc4` | `48 8f 40 f8` | ldr x8,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5acc8"></a> `00b5acc8` | `e8 02 00 b4` | cbz x8,0x00b5ad24 | `CONDITIONAL_JUMP`
<a id="insn-00b5accc"></a> `00b5accc` | `19 23 00 91` | add x25,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00b5acd0"></a> `00b5acd0` | `02 00 00 14` | b 0x00b5acd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5acd4"></a> `00b5acd4` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00b5acd8"></a> `00b5acd8` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b5acdc"></a> `00b5acdc` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00b5ace0"></a> `00b5ace0` | `a9 00 00 54` | b.ls 0x00b5acf4 | `CONDITIONAL_JUMP`
<a id="insn-00b5ace4"></a> `00b5ace4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5ace8"></a> `00b5ace8` | `69 02 00 b4` | cbz x9,0x00b5ad34 | `CONDITIONAL_JUMP`
<a id="insn-00b5acec"></a> `00b5acec` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b5acf0"></a> `00b5acf0` | `f9 ff ff 17` | b 0x00b5acd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5acf4"></a> `00b5acf4` | `82 00 00 54` | b.cs 0x00b5ad04 | `CONDITIONAL_JUMP`
<a id="insn-00b5acf8"></a> `00b5acf8` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b5acfc"></a> `00b5acfc` | `29 8f 40 f8` | ldr x9,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5ad00"></a> `00b5ad00` | `a9 fe ff b5` | cbnz x9,0x00b5acd4 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad04"></a> `00b5ad04` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00b5ad08"></a> `00b5ad08` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00b5ad0c"></a> `00b5ad0c` | `37 04 00 b5` | cbnz x23,0x00b5ad90 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad10"></a> `00b5ad10` | `0d 00 00 14` | b 0x00b5ad44 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ad14"></a> `00b5ad14` | `15 15 40 f9` | ldr x21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ad18"></a> `00b5ad18` | `cb ff ff 17` | b 0x00b5ac44 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ad1c"></a> `00b5ad1c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00b5ad20"></a> `00b5ad20` | `d0 ff ff 17` | b 0x00b5ac60 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ad24"></a> `00b5ad24` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-00b5ad28"></a> `00b5ad28` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00b5ad2c"></a> `00b5ad2c` | `37 03 00 b5` | cbnz x23,0x00b5ad90 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad30"></a> `00b5ad30` | `05 00 00 14` | b 0x00b5ad44 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ad34"></a> `00b5ad34` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00b5ad38"></a> `00b5ad38` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b5ad3c"></a> `00b5ad3c` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00b5ad40"></a> `00b5ad40` | `97 02 00 b5` | cbnz x23,0x00b5ad90 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad44"></a> `00b5ad44` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00b5ad48"></a> `00b5ad48` | `be 00 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ad4c"></a> `00b5ad4c` | `16 7c 02 a9` | stp x22,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ad50"></a> `00b5ad50` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00b5ad54"></a> `00b5ad54` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ad58"></a> `00b5ad58` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00b5ad5c"></a> `00b5ad5c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00b5ad60"></a> `00b5ad60` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b5ad64"></a> `00b5ad64` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b5ad68"></a> `00b5ad68` | `88 00 00 b4` | cbz x8,0x00b5ad78 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad6c"></a> `00b5ad6c` | `08 03 00 f9` | str x8,[x24] | `FALL_THROUGH`
<a id="insn-00b5ad70"></a> `00b5ad70` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00b5ad74"></a> `00b5ad74` | `02 00 00 14` | b 0x00b5ad7c | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ad78"></a> `00b5ad78` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00b5ad7c"></a> `00b5ad7c` | `00 07 40 f9` | ldr x0,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00b5ad80"></a> `00b5ad80` | `78 0e 02 94` | bl 0x00bde760 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ad84"></a> `00b5ad84` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ad88"></a> `00b5ad88` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5ad8c"></a> `00b5ad8c` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ad90"></a> `00b5ad90` | `f5 16 00 f9` | str x21,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b5ad94"></a> `00b5ad94` | `74 f6 ff b4` | cbz x20,0x00b5ac60 | `CONDITIONAL_JUMP`
<a id="insn-00b5ad98"></a> `00b5ad98` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00b5ad9c"></a> `00b5ad9c` | `b1 ff ff 17` | b 0x00b5ac60 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b5abbc`](#insn-00b5abbc) 範囲 `[['00b5abbc', '00b5ac0b']]`
  - `CONDITIONAL_JUMP` [`00b5ac08`](#insn-00b5ac08) → [`00b5ac40`](#insn-00b5ac40)
  - `FALL_THROUGH` [`00b5ac08`](#insn-00b5ac08) → [`00b5ac0c`](#insn-00b5ac0c)
- ブロック [`00b5ac0c`](#insn-00b5ac0c) 範囲 `[['00b5ac0c', '00b5ac0f']]`
  - `FALL_THROUGH` [`00b5ac0c`](#insn-00b5ac0c) → [`00b5ac10`](#insn-00b5ac10)
- ブロック [`00b5ac10`](#insn-00b5ac10) 範囲 `[['00b5ac10', '00b5ac17']]`
  - `FALL_THROUGH` [`00b5ac14`](#insn-00b5ac14) → [`00b5ac18`](#insn-00b5ac18)
- ブロック [`00b5ac18`](#insn-00b5ac18) 範囲 `[['00b5ac18', '00b5ac27']]`
  - `CONDITIONAL_JUMP` [`00b5ac24`](#insn-00b5ac24) → [`00b5ac10`](#insn-00b5ac10)
  - `FALL_THROUGH` [`00b5ac24`](#insn-00b5ac24) → [`00b5ac28`](#insn-00b5ac28)
- ブロック [`00b5ac28`](#insn-00b5ac28) 範囲 `[['00b5ac28', '00b5ac33']]`
  - `CONDITIONAL_JUMP` [`00b5ac30`](#insn-00b5ac30) → [`00b5ac40`](#insn-00b5ac40)
  - `FALL_THROUGH` [`00b5ac30`](#insn-00b5ac30) → [`00b5ac34`](#insn-00b5ac34)
- ブロック [`00b5ac34`](#insn-00b5ac34) 範囲 `[['00b5ac34', '00b5ac3f']]`
  - `CONDITIONAL_JUMP` [`00b5ac3c`](#insn-00b5ac3c) → [`00b5ad14`](#insn-00b5ad14)
  - `FALL_THROUGH` [`00b5ac3c`](#insn-00b5ac3c) → [`00b5ac40`](#insn-00b5ac40)
- ブロック [`00b5ac40`](#insn-00b5ac40) 範囲 `[['00b5ac40', '00b5ac43']]`
  - `FALL_THROUGH` [`00b5ac40`](#insn-00b5ac40) → [`00b5ac44`](#insn-00b5ac44)
- ブロック [`00b5ac44`](#insn-00b5ac44) 範囲 `[['00b5ac44', '00b5ac4f']]`
  - `CONDITIONAL_JUMP` [`00b5ac4c`](#insn-00b5ac4c) → [`00b5ac84`](#insn-00b5ac84)
  - `FALL_THROUGH` [`00b5ac4c`](#insn-00b5ac4c) → [`00b5ac50`](#insn-00b5ac50)
- ブロック [`00b5ac50`](#insn-00b5ac50) 範囲 `[['00b5ac50', '00b5ac53']]`
  - `CONDITIONAL_JUMP` [`00b5ac50`](#insn-00b5ac50) → [`00b5ac58`](#insn-00b5ac58)
  - `FALL_THROUGH` [`00b5ac50`](#insn-00b5ac50) → [`00b5ac54`](#insn-00b5ac54)
- ブロック [`00b5ac54`](#insn-00b5ac54) 範囲 `[['00b5ac54', '00b5ac57']]`
  - `FALL_THROUGH` [`00b5ac54`](#insn-00b5ac54) → [`00b5ac58`](#insn-00b5ac58)
- ブロック [`00b5ac58`](#insn-00b5ac58) 範囲 `[['00b5ac58', '00b5ac5f']]`
  - `FALL_THROUGH` [`00b5ac5c`](#insn-00b5ac5c) → [`00b5ac60`](#insn-00b5ac60)
- ブロック [`00b5ac60`](#insn-00b5ac60) 範囲 `[['00b5ac60', '00b5ac83']]`
- ブロック [`00b5ac84`](#insn-00b5ac84) 範囲 `[['00b5ac84', '00b5ac93']]`
  - `CONDITIONAL_JUMP` [`00b5ac90`](#insn-00b5ac90) → [`00b5ad1c`](#insn-00b5ad1c)
  - `FALL_THROUGH` [`00b5ac90`](#insn-00b5ac90) → [`00b5ac94`](#insn-00b5ac94)
- ブロック [`00b5ac94`](#insn-00b5ac94) 範囲 `[['00b5ac94', '00b5acab']]`
  - `FALL_THROUGH` [`00b5aca8`](#insn-00b5aca8) → [`00b5acac`](#insn-00b5acac)
- ブロック [`00b5acac`](#insn-00b5acac) 範囲 `[['00b5acac', '00b5accb']]`
  - `CONDITIONAL_JUMP` [`00b5acc8`](#insn-00b5acc8) → [`00b5ad24`](#insn-00b5ad24)
  - `FALL_THROUGH` [`00b5acc8`](#insn-00b5acc8) → [`00b5accc`](#insn-00b5accc)
- ブロック [`00b5accc`](#insn-00b5accc) 範囲 `[['00b5accc', '00b5acd3']]`
  - `UNCONDITIONAL_JUMP` [`00b5acd0`](#insn-00b5acd0) → [`00b5acd8`](#insn-00b5acd8)
- ブロック [`00b5acd4`](#insn-00b5acd4) 範囲 `[['00b5acd4', '00b5acd7']]`
  - `FALL_THROUGH` [`00b5acd4`](#insn-00b5acd4) → [`00b5acd8`](#insn-00b5acd8)
- ブロック [`00b5acd8`](#insn-00b5acd8) 範囲 `[['00b5acd8', '00b5ace3']]`
  - `CONDITIONAL_JUMP` [`00b5ace0`](#insn-00b5ace0) → [`00b5acf4`](#insn-00b5acf4)
  - `FALL_THROUGH` [`00b5ace0`](#insn-00b5ace0) → [`00b5ace4`](#insn-00b5ace4)
- ブロック [`00b5ace4`](#insn-00b5ace4) 範囲 `[['00b5ace4', '00b5aceb']]`
  - `CONDITIONAL_JUMP` [`00b5ace8`](#insn-00b5ace8) → [`00b5ad34`](#insn-00b5ad34)
  - `FALL_THROUGH` [`00b5ace8`](#insn-00b5ace8) → [`00b5acec`](#insn-00b5acec)
- ブロック [`00b5acec`](#insn-00b5acec) 範囲 `[['00b5acec', '00b5acf3']]`
  - `UNCONDITIONAL_JUMP` [`00b5acf0`](#insn-00b5acf0) → [`00b5acd4`](#insn-00b5acd4)
- ブロック [`00b5acf4`](#insn-00b5acf4) 範囲 `[['00b5acf4', '00b5acf7']]`
  - `CONDITIONAL_JUMP` [`00b5acf4`](#insn-00b5acf4) → [`00b5ad04`](#insn-00b5ad04)
  - `FALL_THROUGH` [`00b5acf4`](#insn-00b5acf4) → [`00b5acf8`](#insn-00b5acf8)
- ブロック [`00b5acf8`](#insn-00b5acf8) 範囲 `[['00b5acf8', '00b5ad03']]`
  - `CONDITIONAL_JUMP` [`00b5ad00`](#insn-00b5ad00) → [`00b5acd4`](#insn-00b5acd4)
  - `FALL_THROUGH` [`00b5ad00`](#insn-00b5ad00) → [`00b5ad04`](#insn-00b5ad04)
- ブロック [`00b5ad04`](#insn-00b5ad04) 範囲 `[['00b5ad04', '00b5ad0f']]`
  - `CONDITIONAL_JUMP` [`00b5ad0c`](#insn-00b5ad0c) → [`00b5ad90`](#insn-00b5ad90)
  - `FALL_THROUGH` [`00b5ad0c`](#insn-00b5ad0c) → [`00b5ad10`](#insn-00b5ad10)
- ブロック [`00b5ad10`](#insn-00b5ad10) 範囲 `[['00b5ad10', '00b5ad13']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad10`](#insn-00b5ad10) → [`00b5ad44`](#insn-00b5ad44)
- ブロック [`00b5ad14`](#insn-00b5ad14) 範囲 `[['00b5ad14', '00b5ad1b']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad18`](#insn-00b5ad18) → [`00b5ac44`](#insn-00b5ac44)
- ブロック [`00b5ad1c`](#insn-00b5ad1c) 範囲 `[['00b5ad1c', '00b5ad23']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad20`](#insn-00b5ad20) → [`00b5ac60`](#insn-00b5ac60)
- ブロック [`00b5ad24`](#insn-00b5ad24) 範囲 `[['00b5ad24', '00b5ad2f']]`
  - `CONDITIONAL_JUMP` [`00b5ad2c`](#insn-00b5ad2c) → [`00b5ad90`](#insn-00b5ad90)
  - `FALL_THROUGH` [`00b5ad2c`](#insn-00b5ad2c) → [`00b5ad30`](#insn-00b5ad30)
- ブロック [`00b5ad30`](#insn-00b5ad30) 範囲 `[['00b5ad30', '00b5ad33']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad30`](#insn-00b5ad30) → [`00b5ad44`](#insn-00b5ad44)
- ブロック [`00b5ad34`](#insn-00b5ad34) 範囲 `[['00b5ad34', '00b5ad43']]`
  - `CONDITIONAL_JUMP` [`00b5ad40`](#insn-00b5ad40) → [`00b5ad90`](#insn-00b5ad90)
  - `FALL_THROUGH` [`00b5ad40`](#insn-00b5ad40) → [`00b5ad44`](#insn-00b5ad44)
- ブロック [`00b5ad44`](#insn-00b5ad44) 範囲 `[['00b5ad44', '00b5ad6b']]`
  - `CONDITIONAL_JUMP` [`00b5ad68`](#insn-00b5ad68) → [`00b5ad78`](#insn-00b5ad78)
  - `FALL_THROUGH` [`00b5ad68`](#insn-00b5ad68) → [`00b5ad6c`](#insn-00b5ad6c)
- ブロック [`00b5ad6c`](#insn-00b5ad6c) 範囲 `[['00b5ad6c', '00b5ad77']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad74`](#insn-00b5ad74) → [`00b5ad7c`](#insn-00b5ad7c)
- ブロック [`00b5ad78`](#insn-00b5ad78) 範囲 `[['00b5ad78', '00b5ad7b']]`
  - `FALL_THROUGH` [`00b5ad78`](#insn-00b5ad78) → [`00b5ad7c`](#insn-00b5ad7c)
- ブロック [`00b5ad7c`](#insn-00b5ad7c) 範囲 `[['00b5ad7c', '00b5ad87']]`
  - `FALL_THROUGH` [`00b5ad84`](#insn-00b5ad84) → [`00b5ad88`](#insn-00b5ad88)
- ブロック [`00b5ad88`](#insn-00b5ad88) 範囲 `[['00b5ad88', '00b5ad8f']]`
  - `FALL_THROUGH` [`00b5ad8c`](#insn-00b5ad8c) → [`00b5ad90`](#insn-00b5ad90)
- ブロック [`00b5ad90`](#insn-00b5ad90) 範囲 `[['00b5ad90', '00b5ad97']]`
  - `CONDITIONAL_JUMP` [`00b5ad94`](#insn-00b5ad94) → [`00b5ac60`](#insn-00b5ac60)
  - `FALL_THROUGH` [`00b5ad94`](#insn-00b5ad94) → [`00b5ad98`](#insn-00b5ad98)
- ブロック [`00b5ad98`](#insn-00b5ad98) 範囲 `[['00b5ad98', '00b5ad9f']]`
  - `UNCONDITIONAL_JUMP` [`00b5ad9c`](#insn-00b5ad9c) → [`00b5ac60`](#insn-00b5ac60)

## 命令位置別の参照

- [`00b5abbc`](#insn-00b5abbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5abc0`](#insn-00b5abc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5abc4`](#insn-00b5abc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5abc8`](#insn-00b5abc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5abcc`](#insn-00b5abcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5abd8`](#insn-00b5abd8) → `00c1bb70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5abe4`](#insn-00b5abe4) → `010a1418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00b5abec`](#insn-00b5abec) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00b5abf0`](#insn-00b5abf0) → `010a1418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00b5abf8`](#insn-00b5abf8) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac00`](#insn-00b5ac00) → `00c1bb78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5ac04`](#insn-00b5ac04) → `010a1408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ac08`](#insn-00b5ac08) → [`00b5ac40`](#insn-00b5ac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac24`](#insn-00b5ac24) → [`00b5ac10`](#insn-00b5ac10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac30`](#insn-00b5ac30) → [`00b5ac40`](#insn-00b5ac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac3c`](#insn-00b5ac3c) → [`00b5ad14`](#insn-00b5ad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac48`](#insn-00b5ac48) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac4c`](#insn-00b5ac4c) → [`00b5ac84`](#insn-00b5ac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac50`](#insn-00b5ac50) → [`00b5ac58`](#insn-00b5ac58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac5c`](#insn-00b5ac5c) → [`00be0990`](../00be0/00be0990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0990` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac64`](#insn-00b5ac64) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac6c`](#insn-00b5ac6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac70`](#insn-00b5ac70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac74`](#insn-00b5ac74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac78`](#insn-00b5ac78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac88`](#insn-00b5ac88) → [`00be09d0`](../00be0/00be09d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be09d0` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac90`](#insn-00b5ac90) → [`00b5ad1c`](#insn-00b5ad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ac98`](#insn-00b5ac98) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b5aca8`](#insn-00b5aca8) → [`00be0a90`](../00be0/00be0a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0a90` · 推定シンボル `None` · 推定型 `None`
- [`00b5acb0`](#insn-00b5acb0) → `0029d084`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b5acbc`](#insn-00b5acbc) → [`00bde2b0`](../00bde/00bde2b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2b0` · 推定シンボル `None` · 推定型 `None`
- [`00b5acc4`](#insn-00b5acc4) → `010a1408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5acc8`](#insn-00b5acc8) → [`00b5ad24`](#insn-00b5ad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5acd0`](#insn-00b5acd0) → [`00b5acd8`](#insn-00b5acd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ace0`](#insn-00b5ace0) → [`00b5acf4`](#insn-00b5acf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ace8`](#insn-00b5ace8) → [`00b5ad34`](#insn-00b5ad34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5acf0`](#insn-00b5acf0) → [`00b5acd4`](#insn-00b5acd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5acf4`](#insn-00b5acf4) → [`00b5ad04`](#insn-00b5ad04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad00`](#insn-00b5ad00) → [`00b5acd4`](#insn-00b5acd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad0c`](#insn-00b5ad0c) → [`00b5ad90`](#insn-00b5ad90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad10`](#insn-00b5ad10) → [`00b5ad44`](#insn-00b5ad44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad18`](#insn-00b5ad18) → [`00b5ac44`](#insn-00b5ac44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad20`](#insn-00b5ad20) → [`00b5ac60`](#insn-00b5ac60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad28`](#insn-00b5ad28) → `010a1408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ad2c`](#insn-00b5ad2c) → [`00b5ad90`](#insn-00b5ad90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad30`](#insn-00b5ad30) → [`00b5ad44`](#insn-00b5ad44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad40`](#insn-00b5ad40) → [`00b5ad90`](#insn-00b5ad90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad48`](#insn-00b5ad48) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad5c`](#insn-00b5ad5c) → `010a1400`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00b5ad68`](#insn-00b5ad68) → [`00b5ad78`](#insn-00b5ad78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad6c`](#insn-00b5ad6c) → `010a1400`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00b5ad74`](#insn-00b5ad74) → [`00b5ad7c`](#insn-00b5ad7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad7c`](#insn-00b5ad7c) → `010a1408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ad80`](#insn-00b5ad80) → [`00bde760`](../00bde/00bde760.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde760` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad84`](#insn-00b5ad84) → `010a1410`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ad8c`](#insn-00b5ad8c) → `010a1410`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ad94`](#insn-00b5ad94) → [`00b5ac60`](#insn-00b5ac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ad9c`](#insn-00b5ad9c) → [`00b5ac60`](#insn-00b5ac60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5abbc`](#insn-00b5abbc)

~~~json
{
  "source": "00b5abbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5abc0`](#insn-00b5abc0)

~~~json
{
  "source": "00b5abc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5abc4`](#insn-00b5abc4)

~~~json
{
  "source": "00b5abc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5abc8`](#insn-00b5abc8)

~~~json
{
  "source": "00b5abc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5abcc`](#insn-00b5abcc)

~~~json
{
  "source": "00b5abcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5abd8`](#insn-00b5abd8)

~~~json
{
  "source": "00b5abd8",
  "target": "00c1bb70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bb70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5abe4`](#insn-00b5abe4)

~~~json
{
  "source": "00b5abe4",
  "target": "010a1418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5abec`](#insn-00b5abec)

~~~json
{
  "source": "00b5abec",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5abf0`](#insn-00b5abf0)

~~~json
{
  "source": "00b5abf0",
  "target": "010a1418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5abf8`](#insn-00b5abf8)

~~~json
{
  "source": "00b5abf8",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ac00`](#insn-00b5ac00)

~~~json
{
  "source": "00b5ac00",
  "target": "00c1bb78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bb78",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5ac04`](#insn-00b5ac04)

~~~json
{
  "source": "00b5ac04",
  "target": "010a1408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1408",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ac08`](#insn-00b5ac08)

~~~json
{
  "source": "00b5ac08",
  "target": "00b5ac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac24`](#insn-00b5ac24)

~~~json
{
  "source": "00b5ac24",
  "target": "00b5ac10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac30`](#insn-00b5ac30)

~~~json
{
  "source": "00b5ac30",
  "target": "00b5ac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac3c`](#insn-00b5ac3c)

~~~json
{
  "source": "00b5ac3c",
  "target": "00b5ad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac48`](#insn-00b5ac48)

~~~json
{
  "source": "00b5ac48",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ac4c`](#insn-00b5ac4c)

~~~json
{
  "source": "00b5ac4c",
  "target": "00b5ac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac50`](#insn-00b5ac50)

~~~json
{
  "source": "00b5ac50",
  "target": "00b5ac58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac5c`](#insn-00b5ac5c)

~~~json
{
  "source": "00b5ac5c",
  "target": "00be0990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ac64`](#insn-00b5ac64)

~~~json
{
  "source": "00b5ac64",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ac6c`](#insn-00b5ac6c)

~~~json
{
  "source": "00b5ac6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac70`](#insn-00b5ac70)

~~~json
{
  "source": "00b5ac70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac74`](#insn-00b5ac74)

~~~json
{
  "source": "00b5ac74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac78`](#insn-00b5ac78)

~~~json
{
  "source": "00b5ac78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac88`](#insn-00b5ac88)

~~~json
{
  "source": "00b5ac88",
  "target": "00be09d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ac90`](#insn-00b5ac90)

~~~json
{
  "source": "00b5ac90",
  "target": "00b5ad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ac98`](#insn-00b5ac98)

~~~json
{
  "source": "00b5ac98",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5aca8`](#insn-00b5aca8)

~~~json
{
  "source": "00b5aca8",
  "target": "00be0a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5acb0`](#insn-00b5acb0)

~~~json
{
  "source": "00b5acb0",
  "target": "0029d084",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029d084",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "4372656174696e67204175746820257020666f722041707020257000",
  "capture_start": "0029d084",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b5acbc`](#insn-00b5acbc)

~~~json
{
  "source": "00b5acbc",
  "target": "00bde2b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5acc4`](#insn-00b5acc4)

~~~json
{
  "source": "00b5acc4",
  "target": "010a1408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1408",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5acc8`](#insn-00b5acc8)

~~~json
{
  "source": "00b5acc8",
  "target": "00b5ad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5acd0`](#insn-00b5acd0)

~~~json
{
  "source": "00b5acd0",
  "target": "00b5acd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ace0`](#insn-00b5ace0)

~~~json
{
  "source": "00b5ace0",
  "target": "00b5acf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ace8`](#insn-00b5ace8)

~~~json
{
  "source": "00b5ace8",
  "target": "00b5ad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5acf0`](#insn-00b5acf0)

~~~json
{
  "source": "00b5acf0",
  "target": "00b5acd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5acf4`](#insn-00b5acf4)

~~~json
{
  "source": "00b5acf4",
  "target": "00b5ad04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad00`](#insn-00b5ad00)

~~~json
{
  "source": "00b5ad00",
  "target": "00b5acd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad0c`](#insn-00b5ad0c)

~~~json
{
  "source": "00b5ad0c",
  "target": "00b5ad90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad10`](#insn-00b5ad10)

~~~json
{
  "source": "00b5ad10",
  "target": "00b5ad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad18`](#insn-00b5ad18)

~~~json
{
  "source": "00b5ad18",
  "target": "00b5ac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad20`](#insn-00b5ad20)

~~~json
{
  "source": "00b5ad20",
  "target": "00b5ac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad28`](#insn-00b5ad28)

~~~json
{
  "source": "00b5ad28",
  "target": "010a1408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1408",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad2c`](#insn-00b5ad2c)

~~~json
{
  "source": "00b5ad2c",
  "target": "00b5ad90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad30`](#insn-00b5ad30)

~~~json
{
  "source": "00b5ad30",
  "target": "00b5ad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad40`](#insn-00b5ad40)

~~~json
{
  "source": "00b5ad40",
  "target": "00b5ad90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad48`](#insn-00b5ad48)

~~~json
{
  "source": "00b5ad48",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ad5c`](#insn-00b5ad5c)

~~~json
{
  "source": "00b5ad5c",
  "target": "010a1400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1400",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad68`](#insn-00b5ad68)

~~~json
{
  "source": "00b5ad68",
  "target": "00b5ad78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad6c`](#insn-00b5ad6c)

~~~json
{
  "source": "00b5ad6c",
  "target": "010a1400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1400",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad74`](#insn-00b5ad74)

~~~json
{
  "source": "00b5ad74",
  "target": "00b5ad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad7c`](#insn-00b5ad7c)

~~~json
{
  "source": "00b5ad7c",
  "target": "010a1408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1408",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad80`](#insn-00b5ad80)

~~~json
{
  "source": "00b5ad80",
  "target": "00bde760",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ad84`](#insn-00b5ad84)

~~~json
{
  "source": "00b5ad84",
  "target": "010a1410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1410",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad8c`](#insn-00b5ad8c)

~~~json
{
  "source": "00b5ad8c",
  "target": "010a1410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1410",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ad94`](#insn-00b5ad94)

~~~json
{
  "source": "00b5ad94",
  "target": "00b5ac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ad9c`](#insn-00b5ad9c)

~~~json
{
  "source": "00b5ad9c",
  "target": "00b5ac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
