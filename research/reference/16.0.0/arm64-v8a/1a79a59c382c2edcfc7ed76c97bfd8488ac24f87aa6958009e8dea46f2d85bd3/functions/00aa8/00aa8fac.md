# 00aa8fac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a4af88`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-d71b72cef85e2b16feeef32c5495a618)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa91a8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa9/00aa91a8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-dfb3fdfe402c9b48563b7e2f1fdecb53)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa8fac",
  "name": "FUN_00aa8fac",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17edc4ad4be8c15296ae8fe1599524eea718f3206d2cf0a3d7837317564c9e8d",
  "source_text_sha256": "17edc4ad4be8c15296ae8fe1599524eea718f3206d2cf0a3d7837317564c9e8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa8fac",
        "00aa9197"
      ],
      [
        "00aa9228",
        "00aa922b"
      ]
    ],
    "bytes_sha256": "3d43b7e85d3bb168f9667d3a534a1e511378c677c1094b8a2cd9bcc6cc035ec1",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa3c28](../00aa3/00aa3c28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [0087925c](../00879/0087925c.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a430](../00c5a/00c5a430.md)
- [00c5a440](../00c5a/00c5a440.md)

## 関連文字列（未確認候補）

~~~text
"BcResExUnit"
"CharaID"
"Price"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2079 bytes

~~~c

void FUN_00aa8fac(int param_1,ulong param_2)

{
  long lVar1;
  long lVar2;
  undefined4 local_e0 [2];
  char *local_d8;
  char *local_c8;
  undefined4 local_c0 [2];
  undefined8 local_b8;
  char *local_a8;
  undefined4 local_a0 [2];
  undefined8 local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  char *local_68;
  undefined4 local_60 [2];
  undefined8 local_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  local_c8 = "sec1_type";
  local_c0[0] = 0;
  local_b8 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "CharaID";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_a0[0] = 0;
  local_a8 = "sec1_id";
  local_98 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(long)param_1;
  _ZN8firebase7VariantaSEOS0_(local_a0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_80[0] = 0;
  local_88 = "sec2_type";
  local_78 = 0;
                    /* catch() { ... } // from try @ 00aa8e8c with catch @ 00aa9094 */
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "Price";
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_60[0] = 0;
  local_68 = "sec2_id";
  local_58 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(param_2 & 1);
  _ZN8firebase7VariantaSEOS0_(local_60,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514b8();
  FUN_0087925c(*(undefined8 *)(lVar2 + 0x22b0),"BcResExUnit",&local_c8,4);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_60,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_c0,0);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa8fac"></a> `00aa8fac` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aa8fb0"></a> `00aa8fb0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa8fb4"></a> `00aa8fb4` | `f7 5b 00 f9` | str x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa8fb8"></a> `00aa8fb8` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aa8fbc"></a> `00aa8fbc` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aa8fc0"></a> `00aa8fc0` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00aa8fc4"></a> `00aa8fc4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aa8fc8"></a> `00aa8fc8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aa8fcc"></a> `00aa8fcc` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa8fd0"></a> `00aa8fd0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aa8fd4"></a> `00aa8fd4` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa8fd8"></a> `00aa8fd8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa8fdc"></a> `00aa8fdc` | `28 c0 ff d0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aa8fe0"></a> `00aa8fe0` | `08 d1 2a 91` | add x8,x8,#0xab4 | `FALL_THROUGH`
<a id="insn-00aa8fe4"></a> `00aa8fe4` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aa8fe8"></a> `00aa8fe8` | `ff 23 00 b9` | str wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa8fec"></a> `00aa8fec` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aa8ff0"></a> `00aa8ff0` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aa8ff4"></a> `00aa8ff4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa8ff8"></a> `00aa8ff8` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aa8ffc"></a> `00aa8ffc` | `0d c5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9000"></a> `00aa9000` | `e8 bf ff d0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aa9004"></a> `00aa9004` | `08 11 39 91` | add x8,x8,#0xe44 | `FALL_THROUGH`
<a id="insn-00aa9008"></a> `00aa9008` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aa900c"></a> `00aa900c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aa9010"></a> `00aa9010` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa9014"></a> `00aa9014` | `0b c5 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9018"></a> `00aa9018` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa901c"></a> `00aa901c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa9020"></a> `00aa9020` | `04 c5 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9024"></a> `00aa9024` | `48 c0 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aa9028"></a> `00aa9028` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00aa902c"></a> `00aa902c` | `ff 43 00 b9` | str wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa9030"></a> `00aa9030` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aa9034"></a> `00aa9034` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa9038"></a> `00aa9038` | `15 81 00 91` | add x21,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aa903c"></a> `00aa903c` | `14 a1 00 91` | add x20,x8,#0x28 | `FALL_THROUGH`
<a id="insn-00aa9040"></a> `00aa9040` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aa9044"></a> `00aa9044` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aa9048"></a> `00aa9048` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa904c"></a> `00aa904c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aa9050"></a> `00aa9050` | `f8 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9054"></a> `00aa9054` | `c8 7e 40 93` | sxtw x8,w22 | `FALL_THROUGH`
<a id="insn-00aa9058"></a> `00aa9058` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aa905c"></a> `00aa905c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa9060"></a> `00aa9060` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa9064"></a> `00aa9064` | `f7 c4 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9068"></a> `00aa9068` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa906c"></a> `00aa906c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa9070"></a> `00aa9070` | `f0 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9074"></a> `00aa9074` | `e8 bf ff d0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aa9078"></a> `00aa9078` | `08 79 27 91` | add x8,x8,#0x9de | `FALL_THROUGH`
<a id="insn-00aa907c"></a> `00aa907c` | `ff 63 00 b9` | str wzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa9080"></a> `00aa9080` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aa9084"></a> `00aa9084` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa9088"></a> `00aa9088` | `15 01 01 91` | add x21,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00aa908c"></a> `00aa908c` | `14 21 01 91` | add x20,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00aa9090"></a> `00aa9090` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aa9094"></a> `00aa9094` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aa9098"></a> `00aa9098` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa909c"></a> `00aa909c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aa90a0"></a> `00aa90a0` | `e4 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa90a4"></a> `00aa90a4` | `e8 bf ff f0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aa90a8"></a> `00aa90a8` | `08 81 07 91` | add x8,x8,#0x1e0 | `FALL_THROUGH`
<a id="insn-00aa90ac"></a> `00aa90ac` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aa90b0"></a> `00aa90b0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa90b4"></a> `00aa90b4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa90b8"></a> `00aa90b8` | `e2 c4 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa90bc"></a> `00aa90bc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa90c0"></a> `00aa90c0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa90c4"></a> `00aa90c4` | `db c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa90c8"></a> `00aa90c8` | `28 c0 ff d0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aa90cc"></a> `00aa90cc` | `08 ad 2f 91` | add x8,x8,#0xbeb | `FALL_THROUGH`
<a id="insn-00aa90d0"></a> `00aa90d0` | `ff 83 00 b9` | str wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aa90d4"></a> `00aa90d4` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aa90d8"></a> `00aa90d8` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa90dc"></a> `00aa90dc` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aa90e0"></a> `00aa90e0` | `14 a1 01 91` | add x20,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00aa90e4"></a> `00aa90e4` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aa90e8"></a> `00aa90e8` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aa90ec"></a> `00aa90ec` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa90f0"></a> `00aa90f0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aa90f4"></a> `00aa90f4` | `cf c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa90f8"></a> `00aa90f8` | `68 02 40 92` | and x8,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00aa90fc"></a> `00aa90fc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aa9100"></a> `00aa9100` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa9104"></a> `00aa9104` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa9108"></a> `00aa9108` | `ce c4 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa910c"></a> `00aa910c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aa9110"></a> `00aa9110` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa9114"></a> `00aa9114` | `c7 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9118"></a> `00aa9118` | `e8 a0 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa911c"></a> `00aa911c` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aa9120"></a> `00aa9120` | `41 c0 ff b0` | adrp x1,0x2b2000 | `FALL_THROUGH`
<a id="insn-00aa9124"></a> `00aa9124` | `21 38 12 91` | add x1,x1,#0x48e | `FALL_THROUGH`
<a id="insn-00aa9128"></a> `00aa9128` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa912c"></a> `00aa912c` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00aa9130"></a> `00aa9130` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa9134"></a> `00aa9134` | `4a 40 f7 97` | bl 0x0087925c | `UNCONDITIONAL_CALL`
<a id="insn-00aa9138"></a> `00aa9138` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aa913c"></a> `00aa913c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa9140"></a> `00aa9140` | `bc c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9144"></a> `00aa9144` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa9148"></a> `00aa9148` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aa914c"></a> `00aa914c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa9150"></a> `00aa9150` | `b8 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9154"></a> `00aa9154` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aa9158"></a> `00aa9158` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa915c"></a> `00aa915c` | `b5 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9160"></a> `00aa9160` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aa9164"></a> `00aa9164` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aa9168"></a> `00aa9168` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa916c"></a> `00aa916c` | `b1 c4 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa9170"></a> `00aa9170` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aa9174"></a> `00aa9174` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa9178"></a> `00aa9178` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa917c"></a> `00aa917c` | `61 05 00 54` | b.ne 0x00aa9228 | `CONDITIONAL_JUMP`
<a id="insn-00aa9180"></a> `00aa9180` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aa9184"></a> `00aa9184` | `f7 5b 40 f9` | ldr x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa9188"></a> `00aa9188` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aa918c"></a> `00aa918c` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa9190"></a> `00aa9190` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aa9194"></a> `00aa9194` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa9228"></a> `00aa9228` | `2e ba 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa8fac`](#insn-00aa8fac) 範囲 `[['00aa8fac', '00aa9093']]`
  - `FALL_THROUGH` [`00aa9090`](#insn-00aa9090) → [`00aa9094`](#insn-00aa9094)
- ブロック [`00aa9094`](#insn-00aa9094) 範囲 `[['00aa9094', '00aa917f']]`
  - `CONDITIONAL_JUMP` [`00aa917c`](#insn-00aa917c) → [`00aa9228`](#insn-00aa9228)
  - `FALL_THROUGH` [`00aa917c`](#insn-00aa917c) → [`00aa9180`](#insn-00aa9180)
- ブロック [`00aa9180`](#insn-00aa9180) 範囲 `[['00aa9180', '00aa9197']]`
- ブロック [`00aa9228`](#insn-00aa9228) 範囲 `[['00aa9228', '00aa922b']]`

## 命令位置別の参照

- [`00aa8fb0`](#insn-00aa8fb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fb4`](#insn-00aa8fb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fb8`](#insn-00aa8fb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fbc`](#insn-00aa8fbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fd8`](#insn-00aa8fd8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fe4`](#insn-00aa8fe4) → `002aeab4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa8fe4`](#insn-00aa8fe4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fe8`](#insn-00aa8fe8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8fec`](#insn-00aa8fec) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8ff0`](#insn-00aa8ff0) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa8ffc`](#insn-00aa8ffc) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9010`](#insn-00aa9010) → `002a7e44`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa9010`](#insn-00aa9010) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9014`](#insn-00aa9014) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa9020`](#insn-00aa9020) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa902c`](#insn-00aa902c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9030`](#insn-00aa9030) → `002b1e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa9030`](#insn-00aa9030) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9040`](#insn-00aa9040) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9044`](#insn-00aa9044) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9050`](#insn-00aa9050) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9060`](#insn-00aa9060) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9064`](#insn-00aa9064) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa9070`](#insn-00aa9070) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa907c`](#insn-00aa907c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9080`](#insn-00aa9080) → `002a79de`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa9080`](#insn-00aa9080) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9090`](#insn-00aa9090) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9094`](#insn-00aa9094) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90a0`](#insn-00aa90a0) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa90b4`](#insn-00aa90b4) → `002a81e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa90b4`](#insn-00aa90b4) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90b8`](#insn-00aa90b8) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa90c4`](#insn-00aa90c4) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa90d0`](#insn-00aa90d0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90d4`](#insn-00aa90d4) → `002afbeb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa90d4`](#insn-00aa90d4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90e4`](#insn-00aa90e4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90e8`](#insn-00aa90e8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa90f4`](#insn-00aa90f4) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9104`](#insn-00aa9104) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9108`](#insn-00aa9108) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa9114`](#insn-00aa9114) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9118`](#insn-00aa9118) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa9124`](#insn-00aa9124) → `002b248e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa9134`](#insn-00aa9134) → [`0087925c`](../00879/0087925c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087925c` · 推定シンボル `None` · 推定型 `None`
- [`00aa9140`](#insn-00aa9140) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9150`](#insn-00aa9150) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa915c`](#insn-00aa915c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa916c`](#insn-00aa916c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa9174`](#insn-00aa9174) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa917c`](#insn-00aa917c) → [`00aa9228`](#insn-00aa9228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9180`](#insn-00aa9180) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9184`](#insn-00aa9184) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9188`](#insn-00aa9188) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa918c`](#insn-00aa918c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa9228`](#insn-00aa9228) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa8fb0`](#insn-00aa8fb0)

~~~json
{
  "source": "00aa8fb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fb4`](#insn-00aa8fb4)

~~~json
{
  "source": "00aa8fb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fb8`](#insn-00aa8fb8)

~~~json
{
  "source": "00aa8fb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fbc`](#insn-00aa8fbc)

~~~json
{
  "source": "00aa8fbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fd8`](#insn-00aa8fd8)

~~~json
{
  "source": "00aa8fd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fe4`](#insn-00aa8fe4)

~~~json
{
  "source": "00aa8fe4",
  "target": "002aeab4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeab4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeab4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa8fe4`](#insn-00aa8fe4)

~~~json
{
  "source": "00aa8fe4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fe8`](#insn-00aa8fe8)

~~~json
{
  "source": "00aa8fe8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8fec`](#insn-00aa8fec)

~~~json
{
  "source": "00aa8fec",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8ff0`](#insn-00aa8ff0)

~~~json
{
  "source": "00aa8ff0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa8ffc`](#insn-00aa8ffc)

~~~json
{
  "source": "00aa8ffc",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9010`](#insn-00aa9010)

~~~json
{
  "source": "00aa9010",
  "target": "002a7e44",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7e44",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "4368617261494400",
  "capture_start": "002a7e44",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa9010`](#insn-00aa9010)

~~~json
{
  "source": "00aa9010",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9014`](#insn-00aa9014)

~~~json
{
  "source": "00aa9014",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9020`](#insn-00aa9020)

~~~json
{
  "source": "00aa9020",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa902c`](#insn-00aa902c)

~~~json
{
  "source": "00aa902c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9030`](#insn-00aa9030)

~~~json
{
  "source": "00aa9030",
  "target": "002b1e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e08",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e08",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa9030`](#insn-00aa9030)

~~~json
{
  "source": "00aa9030",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9040`](#insn-00aa9040)

~~~json
{
  "source": "00aa9040",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9044`](#insn-00aa9044)

~~~json
{
  "source": "00aa9044",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9050`](#insn-00aa9050)

~~~json
{
  "source": "00aa9050",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9060`](#insn-00aa9060)

~~~json
{
  "source": "00aa9060",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9064`](#insn-00aa9064)

~~~json
{
  "source": "00aa9064",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9070`](#insn-00aa9070)

~~~json
{
  "source": "00aa9070",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa907c`](#insn-00aa907c)

~~~json
{
  "source": "00aa907c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9080`](#insn-00aa9080)

~~~json
{
  "source": "00aa9080",
  "target": "002a79de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a79de",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a79de",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa9080`](#insn-00aa9080)

~~~json
{
  "source": "00aa9080",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9090`](#insn-00aa9090)

~~~json
{
  "source": "00aa9090",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9094`](#insn-00aa9094)

~~~json
{
  "source": "00aa9094",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90a0`](#insn-00aa90a0)

~~~json
{
  "source": "00aa90a0",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa90b4`](#insn-00aa90b4)

~~~json
{
  "source": "00aa90b4",
  "target": "002a81e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a81e0",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "507269636500",
  "capture_start": "002a81e0",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa90b4`](#insn-00aa90b4)

~~~json
{
  "source": "00aa90b4",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90b8`](#insn-00aa90b8)

~~~json
{
  "source": "00aa90b8",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa90c4`](#insn-00aa90c4)

~~~json
{
  "source": "00aa90c4",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa90d0`](#insn-00aa90d0)

~~~json
{
  "source": "00aa90d0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90d4`](#insn-00aa90d4)

~~~json
{
  "source": "00aa90d4",
  "target": "002afbeb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afbeb",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afbeb",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa90d4`](#insn-00aa90d4)

~~~json
{
  "source": "00aa90d4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90e4`](#insn-00aa90e4)

~~~json
{
  "source": "00aa90e4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90e8`](#insn-00aa90e8)

~~~json
{
  "source": "00aa90e8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa90f4`](#insn-00aa90f4)

~~~json
{
  "source": "00aa90f4",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9104`](#insn-00aa9104)

~~~json
{
  "source": "00aa9104",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9108`](#insn-00aa9108)

~~~json
{
  "source": "00aa9108",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9114`](#insn-00aa9114)

~~~json
{
  "source": "00aa9114",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9118`](#insn-00aa9118)

~~~json
{
  "source": "00aa9118",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9124`](#insn-00aa9124)

~~~json
{
  "source": "00aa9124",
  "target": "002b248e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b248e",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "42635265734578556e697400",
  "capture_start": "002b248e",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa9134`](#insn-00aa9134)

~~~json
{
  "source": "00aa9134",
  "target": "0087925c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9140`](#insn-00aa9140)

~~~json
{
  "source": "00aa9140",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9150`](#insn-00aa9150)

~~~json
{
  "source": "00aa9150",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa915c`](#insn-00aa915c)

~~~json
{
  "source": "00aa915c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa916c`](#insn-00aa916c)

~~~json
{
  "source": "00aa916c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa9174`](#insn-00aa9174)

~~~json
{
  "source": "00aa9174",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa917c`](#insn-00aa917c)

~~~json
{
  "source": "00aa917c",
  "target": "00aa9228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9180`](#insn-00aa9180)

~~~json
{
  "source": "00aa9180",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9184`](#insn-00aa9184)

~~~json
{
  "source": "00aa9184",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9188`](#insn-00aa9188)

~~~json
{
  "source": "00aa9188",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa918c`](#insn-00aa918c)

~~~json
{
  "source": "00aa918c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa9228`](#insn-00aa9228)

~~~json
{
  "source": "00aa9228",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
