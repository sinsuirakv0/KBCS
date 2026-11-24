# 00aa6abc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a48a98`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48a98.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-e7cb85bc66957ef2288f663041007c26)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa6cb8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa6/00aa6cb8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-f3b985a92c23fa0a3cf9c87458d9a279)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa6abc",
  "name": "FUN_00aa6abc",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f3bbcc15dcc3a7eeb3de8de76ea00570de7db0b9731d6662fffca4c8ad286f6",
  "source_text_sha256": "2f3bbcc15dcc3a7eeb3de8de76ea00570de7db0b9731d6662fffca4c8ad286f6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa6abc",
        "00aa6cbf"
      ],
      [
        "00aa6da0",
        "00aa6da3"
      ]
    ],
    "bytes_sha256": "88e8cdd539b22b831fa6330eb269cab0c1f872dc1657fe5a97233dee883012fb",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa3c28](../00aa3/00aa3c28.md)

## 呼び出し先

- [006ea4b4](../006ea/006ea4b4.md)
- [00784240](../00784/00784240.md)
- [008514b8](../00851/008514b8.md)
- [0087925c](../00879/0087925c.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a430](../00c5a/00c5a430.md)
- [00c5a440](../00c5a/00c5a440.md)
- [00c5a4f0](../00c5a/00c5a4f0.md)

## 関連文字列（未確認候補）

~~~text
"BcResGamatoto"
"Message"
"StageName"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2559 bytes

~~~c

void FUN_00aa6abc(undefined4 param_1,int param_2)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_128 [24];
  byte local_110 [16];
  void *local_100;
  undefined1 auStack_f8 [24];
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
  local_d8 = "StageName";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514b8(&local_c8);
  FUN_006ea4b4(local_110,lVar2 + 0x42ef90,param_1);
  FUN_00784240(auStack_f8,local_110);
                    /* catch() { ... } // from try @ 00aa6bcc with catch @ 00aa6b60 */
  local_a8 = "sec1_id";
  local_a0[0] = 0;
  local_98 = 0;
  _ZN8firebase7VariantaSERKS0_(local_a0,auStack_f8);
  local_88 = "sec2_type";
  local_80[0] = 0;
  local_78 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "Message";
                    /* try { // try from 00aa6bc0 to 00ba6bcb has its CatchHandler @ 00aa6c28 */
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
                    /* try { // try from 00aa6bcc to 00ba6c67 has its CatchHandler @ 00aa6b60 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514b8(&local_c8);
  FUN_00784240(auStack_128,lVar2 + (long)param_2 * 0x78 + 0x44abf8);
  local_68 = "sec2_id";
  local_60[0] = 0;
  local_58 = 0;
  _ZN8firebase7VariantaSERKS0_(local_60,auStack_128);
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_128,0);
                    /* catch() { ... } // from try @ 00aa6bc0 with catch @ 00aa6c28 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_f8,0);
  if ((local_110[0] & 1) != 0) {
    _ZdlPv(local_100);
  }
  lVar2 = FUN_008514b8();
  FUN_0087925c(*(undefined8 *)(lVar2 + 0x22b0),"BcResGamatoto",&local_c8,4);
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
<a id="insn-00aa6abc"></a> `00aa6abc` | `ff c3 04 d1` | sub sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-00aa6ac0"></a> `00aa6ac0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aa6ac4"></a> `00aa6ac4` | `fc 83 00 f9` | str x28,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aa6ac8"></a> `00aa6ac8` | `f6 57 11 a9` | stp x22,x21,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aa6acc"></a> `00aa6acc` | `f4 4f 12 a9` | stp x20,x19,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00aa6ad0"></a> `00aa6ad0` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00aa6ad4"></a> `00aa6ad4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aa6ad8"></a> `00aa6ad8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa6adc"></a> `00aa6adc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa6ae0"></a> `00aa6ae0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aa6ae4"></a> `00aa6ae4` | `f3 a3 01 91` | add x19,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6ae8"></a> `00aa6ae8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa6aec"></a> `00aa6aec` | `48 c0 ff 90` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aa6af0"></a> `00aa6af0` | `08 d1 2a 91` | add x8,x8,#0xab4 | `FALL_THROUGH`
<a id="insn-00aa6af4"></a> `00aa6af4` | `e8 37 00 f9` | str x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aa6af8"></a> `00aa6af8` | `ff 73 00 b9` | str wzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa6afc"></a> `00aa6afc` | `ff 3f 00 f9` | str xzr,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aa6b00"></a> `00aa6b00` | `ff 53 00 b9` | str wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa6b04"></a> `00aa6b04` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6b08"></a> `00aa6b08` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aa6b0c"></a> `00aa6b0c` | `49 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b10"></a> `00aa6b10` | `a8 c0 ff b0` | adrp x8,0x2bb000 | `FALL_THROUGH`
<a id="insn-00aa6b14"></a> `00aa6b14` | `08 a5 32 91` | add x8,x8,#0xca9 | `FALL_THROUGH`
<a id="insn-00aa6b18"></a> `00aa6b18` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aa6b1c"></a> `00aa6b1c` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6b20"></a> `00aa6b20` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aa6b24"></a> `00aa6b24` | `47 ce 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b28"></a> `00aa6b28` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6b2c"></a> `00aa6b2c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6b30"></a> `00aa6b30` | `40 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b34"></a> `00aa6b34` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6b38"></a> `00aa6b38` | `13 81 00 91` | add x19,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aa6b3c"></a> `00aa6b3c` | `5f aa f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b40"></a> `00aa6b40` | `09 b8 50 91` | add x9,x0,#0x42e, LSL #12 | `FALL_THROUGH`
<a id="insn-00aa6b44"></a> `00aa6b44` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aa6b48"></a> `00aa6b48` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00aa6b4c"></a> `00aa6b4c` | `20 41 3e 91` | add x0,x9,#0xf90 | `FALL_THROUGH`
<a id="insn-00aa6b50"></a> `00aa6b50` | `59 0e f1 97` | bl 0x006ea4b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b54"></a> `00aa6b54` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aa6b58"></a> `00aa6b58` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aa6b5c"></a> `00aa6b5c` | `b9 75 f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b60"></a> `00aa6b60` | `48 c0 ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aa6b64"></a> `00aa6b64` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00aa6b68"></a> `00aa6b68` | `f5 a3 01 91` | add x21,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6b6c"></a> `00aa6b6c` | `e8 47 00 f9` | str x8,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aa6b70"></a> `00aa6b70` | `ff 93 00 b9` | str wzr,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa6b74"></a> `00aa6b74` | `ff 4f 00 f9` | str xzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00aa6b78"></a> `00aa6b78` | `a0 a2 00 91` | add x0,x21,#0x28 | `FALL_THROUGH`
<a id="insn-00aa6b7c"></a> `00aa6b7c` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aa6b80"></a> `00aa6b80` | `5c ce 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6b84"></a> `00aa6b84` | `08 c0 ff b0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aa6b88"></a> `00aa6b88` | `08 79 27 91` | add x8,x8,#0x9de | `FALL_THROUGH`
<a id="insn-00aa6b8c"></a> `00aa6b8c` | `b3 02 01 91` | add x19,x21,#0x40 | `FALL_THROUGH`
<a id="insn-00aa6b90"></a> `00aa6b90` | `e8 57 00 f9` | str x8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00aa6b94"></a> `00aa6b94` | `ff b3 00 b9` | str wzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa6b98"></a> `00aa6b98` | `ff 5f 00 f9` | str xzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00aa6b9c"></a> `00aa6b9c` | `ff 53 00 b9` | str wzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa6ba0"></a> `00aa6ba0` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6ba4"></a> `00aa6ba4` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aa6ba8"></a> `00aa6ba8` | `22 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6bac"></a> `00aa6bac` | `c8 c0 ff b0` | adrp x8,0x2bf000 | `FALL_THROUGH`
<a id="insn-00aa6bb0"></a> `00aa6bb0` | `08 99 18 91` | add x8,x8,#0x626 | `FALL_THROUGH`
<a id="insn-00aa6bb4"></a> `00aa6bb4` | `a0 22 01 91` | add x0,x21,#0x48 | `FALL_THROUGH`
<a id="insn-00aa6bb8"></a> `00aa6bb8` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6bbc"></a> `00aa6bbc` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aa6bc0"></a> `00aa6bc0` | `20 ce 06 94` | bl 0x00c5a440 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6bc4"></a> `00aa6bc4` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aa6bc8"></a> `00aa6bc8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6bcc"></a> `00aa6bcc` | `19 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6bd0"></a> `00aa6bd0` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6bd4"></a> `00aa6bd4` | `13 81 01 91` | add x19,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aa6bd8"></a> `00aa6bd8` | `38 aa f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6bdc"></a> `00aa6bdc` | `08 0f 80 52` | mov w8,#0x78 | `FALL_THROUGH`
<a id="insn-00aa6be0"></a> `00aa6be0` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa6be4"></a> `00aa6be4` | `08 29 51 91` | add x8,x8,#0x44a, LSL #12 | `FALL_THROUGH`
<a id="insn-00aa6be8"></a> `00aa6be8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa6bec"></a> `00aa6bec` | `01 e1 2f 91` | add x1,x8,#0xbf8 | `FALL_THROUGH`
<a id="insn-00aa6bf0"></a> `00aa6bf0` | `94 75 f3 97` | bl 0x00784240 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6bf4"></a> `00aa6bf4` | `48 c0 ff b0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aa6bf8"></a> `00aa6bf8` | `08 ad 2f 91` | add x8,x8,#0xbeb | `FALL_THROUGH`
<a id="insn-00aa6bfc"></a> `00aa6bfc` | `f5 a3 01 91` | add x21,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c00"></a> `00aa6c00` | `e8 67 00 f9` | str x8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00aa6c04"></a> `00aa6c04` | `ff d3 00 b9` | str wzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aa6c08"></a> `00aa6c08` | `ff 6f 00 f9` | str xzr,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aa6c0c"></a> `00aa6c0c` | `a0 a2 01 91` | add x0,x21,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c10"></a> `00aa6c10` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa6c14"></a> `00aa6c14` | `37 ce 06 94` | bl 0x00c5a4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c18"></a> `00aa6c18` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa6c1c"></a> `00aa6c1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c20"></a> `00aa6c20` | `04 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c24"></a> `00aa6c24` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aa6c28"></a> `00aa6c28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c2c"></a> `00aa6c2c` | `01 ce 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c30"></a> `00aa6c30` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa6c34"></a> `00aa6c34` | `68 00 00 36` | tbz w8,#0x0,0x00aa6c40 | `CONDITIONAL_JUMP`
<a id="insn-00aa6c38"></a> `00aa6c38` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa6c3c"></a> `00aa6c3c` | `9d c3 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c40"></a> `00aa6c40` | `1e aa f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c44"></a> `00aa6c44` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aa6c48"></a> `00aa6c48` | `01 c0 ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00aa6c4c"></a> `00aa6c4c` | `21 a0 39 91` | add x1,x1,#0xe68 | `FALL_THROUGH`
<a id="insn-00aa6c50"></a> `00aa6c50` | `e2 a3 01 91` | add x2,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c54"></a> `00aa6c54` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00aa6c58"></a> `00aa6c58` | `f3 a3 01 91` | add x19,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c5c"></a> `00aa6c5c` | `80 49 f7 97` | bl 0x0087925c | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c60"></a> `00aa6c60` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c64"></a> `00aa6c64` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c68"></a> `00aa6c68` | `f2 cd 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c6c"></a> `00aa6c6c` | `f3 a3 01 91` | add x19,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c70"></a> `00aa6c70` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aa6c74"></a> `00aa6c74` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c78"></a> `00aa6c78` | `ee cd 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c7c"></a> `00aa6c7c` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aa6c80"></a> `00aa6c80` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c84"></a> `00aa6c84` | `eb cd 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c88"></a> `00aa6c88` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00aa6c8c"></a> `00aa6c8c` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aa6c90"></a> `00aa6c90` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aa6c94"></a> `00aa6c94` | `e7 cd 06 94` | bl 0x00c5a430 | `UNCONDITIONAL_CALL`
<a id="insn-00aa6c98"></a> `00aa6c98` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aa6c9c"></a> `00aa6c9c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa6ca0"></a> `00aa6ca0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa6ca4"></a> `00aa6ca4` | `e1 07 00 54` | b.ne 0x00aa6da0 | `CONDITIONAL_JUMP`
<a id="insn-00aa6ca8"></a> `00aa6ca8` | `f4 4f 52 a9` | ldp x20,x19,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00aa6cac"></a> `00aa6cac` | `fc 83 40 f9` | ldr x28,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00aa6cb0"></a> `00aa6cb0` | `f6 57 51 a9` | ldp x22,x21,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00aa6cb4"></a> `00aa6cb4` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00aa6cb8"></a> `00aa6cb8` | `ff c3 04 91` | add sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-00aa6cbc"></a> `00aa6cbc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa6da0"></a> `00aa6da0` | `50 c3 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa6abc`](#insn-00aa6abc) 範囲 `[['00aa6abc', '00aa6b5f']]`
  - `FALL_THROUGH` [`00aa6b5c`](#insn-00aa6b5c) → [`00aa6b60`](#insn-00aa6b60)
- ブロック [`00aa6b60`](#insn-00aa6b60) 範囲 `[['00aa6b60', '00aa6bbf']]`
  - `FALL_THROUGH` [`00aa6bbc`](#insn-00aa6bbc) → [`00aa6bc0`](#insn-00aa6bc0)
- ブロック [`00aa6bc0`](#insn-00aa6bc0) 範囲 `[['00aa6bc0', '00aa6bcb']]`
  - `FALL_THROUGH` [`00aa6bc8`](#insn-00aa6bc8) → [`00aa6bcc`](#insn-00aa6bcc)
- ブロック [`00aa6bcc`](#insn-00aa6bcc) 範囲 `[['00aa6bcc', '00aa6c27']]`
  - `FALL_THROUGH` [`00aa6c24`](#insn-00aa6c24) → [`00aa6c28`](#insn-00aa6c28)
- ブロック [`00aa6c28`](#insn-00aa6c28) 範囲 `[['00aa6c28', '00aa6c37']]`
  - `CONDITIONAL_JUMP` [`00aa6c34`](#insn-00aa6c34) → [`00aa6c40`](#insn-00aa6c40)
  - `FALL_THROUGH` [`00aa6c34`](#insn-00aa6c34) → [`00aa6c38`](#insn-00aa6c38)
- ブロック [`00aa6c38`](#insn-00aa6c38) 範囲 `[['00aa6c38', '00aa6c3f']]`
  - `FALL_THROUGH` [`00aa6c3c`](#insn-00aa6c3c) → [`00aa6c40`](#insn-00aa6c40)
- ブロック [`00aa6c40`](#insn-00aa6c40) 範囲 `[['00aa6c40', '00aa6ca7']]`
  - `CONDITIONAL_JUMP` [`00aa6ca4`](#insn-00aa6ca4) → [`00aa6da0`](#insn-00aa6da0)
  - `FALL_THROUGH` [`00aa6ca4`](#insn-00aa6ca4) → [`00aa6ca8`](#insn-00aa6ca8)
- ブロック [`00aa6ca8`](#insn-00aa6ca8) 範囲 `[['00aa6ca8', '00aa6cbf']]`
- ブロック [`00aa6da0`](#insn-00aa6da0) 範囲 `[['00aa6da0', '00aa6da3']]`

## 命令位置別の参照

- [`00aa6ac0`](#insn-00aa6ac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ac4`](#insn-00aa6ac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ac8`](#insn-00aa6ac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6acc`](#insn-00aa6acc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ae8`](#insn-00aa6ae8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6af4`](#insn-00aa6af4) → `002aeab4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6af4`](#insn-00aa6af4) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6af8`](#insn-00aa6af8) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6afc`](#insn-00aa6afc) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b00`](#insn-00aa6b00) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b0c`](#insn-00aa6b0c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b20`](#insn-00aa6b20) → `002bbca9`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6b20`](#insn-00aa6b20) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b24`](#insn-00aa6b24) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b30`](#insn-00aa6b30) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b3c`](#insn-00aa6b3c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b50`](#insn-00aa6b50) → [`006ea4b4`](../006ea/006ea4b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006ea4b4` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b5c`](#insn-00aa6b5c) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b6c`](#insn-00aa6b6c) → `002b1e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6b6c`](#insn-00aa6b6c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b70`](#insn-00aa6b70) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b74`](#insn-00aa6b74) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b80`](#insn-00aa6b80) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b90`](#insn-00aa6b90) → `002a79de`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6b90`](#insn-00aa6b90) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b94`](#insn-00aa6b94) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b98`](#insn-00aa6b98) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6b9c`](#insn-00aa6b9c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ba8`](#insn-00aa6ba8) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6bbc`](#insn-00aa6bbc) → `002bf626`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6bbc`](#insn-00aa6bbc) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6bc0`](#insn-00aa6bc0) → [`00c5a440`](../00c5a/00c5a440.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a440` · 推定シンボル `None` · 推定型 `None`
- [`00aa6bcc`](#insn-00aa6bcc) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6bd8`](#insn-00aa6bd8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa6bf0`](#insn-00aa6bf0) → [`00784240`](../00784/00784240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00784240` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c00`](#insn-00aa6c00) → `002afbeb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6c00`](#insn-00aa6c00) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c04`](#insn-00aa6c04) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c08`](#insn-00aa6c08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c14`](#insn-00aa6c14) → [`00c5a4f0`](../00c5a/00c5a4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a4f0` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c20`](#insn-00aa6c20) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c2c`](#insn-00aa6c2c) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c30`](#insn-00aa6c30) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c34`](#insn-00aa6c34) → [`00aa6c40`](#insn-00aa6c40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c38`](#insn-00aa6c38) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c3c`](#insn-00aa6c3c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c40`](#insn-00aa6c40) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c4c`](#insn-00aa6c4c) → `002a6e68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa6c5c`](#insn-00aa6c5c) → [`0087925c`](../00879/0087925c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087925c` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c68`](#insn-00aa6c68) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c78`](#insn-00aa6c78) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c84`](#insn-00aa6c84) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c94`](#insn-00aa6c94) → [`00c5a430`](../00c5a/00c5a430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a430` · 推定シンボル `None` · 推定型 `None`
- [`00aa6c9c`](#insn-00aa6c9c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ca4`](#insn-00aa6ca4) → [`00aa6da0`](#insn-00aa6da0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6ca8`](#insn-00aa6ca8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6cac`](#insn-00aa6cac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6cb0`](#insn-00aa6cb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6cb4`](#insn-00aa6cb4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa6da0`](#insn-00aa6da0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa6ac0`](#insn-00aa6ac0)

~~~json
{
  "source": "00aa6ac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ac4`](#insn-00aa6ac4)

~~~json
{
  "source": "00aa6ac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ac8`](#insn-00aa6ac8)

~~~json
{
  "source": "00aa6ac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6acc`](#insn-00aa6acc)

~~~json
{
  "source": "00aa6acc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ae8`](#insn-00aa6ae8)

~~~json
{
  "source": "00aa6ae8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6af4`](#insn-00aa6af4)

~~~json
{
  "source": "00aa6af4",
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
- 参照命令 [`00aa6af4`](#insn-00aa6af4)

~~~json
{
  "source": "00aa6af4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6af8`](#insn-00aa6af8)

~~~json
{
  "source": "00aa6af8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6afc`](#insn-00aa6afc)

~~~json
{
  "source": "00aa6afc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b00`](#insn-00aa6b00)

~~~json
{
  "source": "00aa6b00",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b0c`](#insn-00aa6b0c)

~~~json
{
  "source": "00aa6b0c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b20`](#insn-00aa6b20)

~~~json
{
  "source": "00aa6b20",
  "target": "002bbca9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bbca9",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "53746167654e616d6500",
  "capture_start": "002bbca9",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa6b20`](#insn-00aa6b20)

~~~json
{
  "source": "00aa6b20",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b24`](#insn-00aa6b24)

~~~json
{
  "source": "00aa6b24",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b30`](#insn-00aa6b30)

~~~json
{
  "source": "00aa6b30",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b3c`](#insn-00aa6b3c)

~~~json
{
  "source": "00aa6b3c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b50`](#insn-00aa6b50)

~~~json
{
  "source": "00aa6b50",
  "target": "006ea4b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b5c`](#insn-00aa6b5c)

~~~json
{
  "source": "00aa6b5c",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b6c`](#insn-00aa6b6c)

~~~json
{
  "source": "00aa6b6c",
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
- 参照命令 [`00aa6b6c`](#insn-00aa6b6c)

~~~json
{
  "source": "00aa6b6c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b70`](#insn-00aa6b70)

~~~json
{
  "source": "00aa6b70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b74`](#insn-00aa6b74)

~~~json
{
  "source": "00aa6b74",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b80`](#insn-00aa6b80)

~~~json
{
  "source": "00aa6b80",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6b90`](#insn-00aa6b90)

~~~json
{
  "source": "00aa6b90",
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
- 参照命令 [`00aa6b90`](#insn-00aa6b90)

~~~json
{
  "source": "00aa6b90",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b94`](#insn-00aa6b94)

~~~json
{
  "source": "00aa6b94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b98`](#insn-00aa6b98)

~~~json
{
  "source": "00aa6b98",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6b9c`](#insn-00aa6b9c)

~~~json
{
  "source": "00aa6b9c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ba8`](#insn-00aa6ba8)

~~~json
{
  "source": "00aa6ba8",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6bbc`](#insn-00aa6bbc)

~~~json
{
  "source": "00aa6bbc",
  "target": "002bf626",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf626",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "4d65737361676500",
  "capture_start": "002bf626",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa6bbc`](#insn-00aa6bbc)

~~~json
{
  "source": "00aa6bbc",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6bc0`](#insn-00aa6bc0)

~~~json
{
  "source": "00aa6bc0",
  "target": "00c5a440",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6bcc`](#insn-00aa6bcc)

~~~json
{
  "source": "00aa6bcc",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6bd8`](#insn-00aa6bd8)

~~~json
{
  "source": "00aa6bd8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6bf0`](#insn-00aa6bf0)

~~~json
{
  "source": "00aa6bf0",
  "target": "00784240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c00`](#insn-00aa6c00)

~~~json
{
  "source": "00aa6c00",
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
- 参照命令 [`00aa6c00`](#insn-00aa6c00)

~~~json
{
  "source": "00aa6c00",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c04`](#insn-00aa6c04)

~~~json
{
  "source": "00aa6c04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c08`](#insn-00aa6c08)

~~~json
{
  "source": "00aa6c08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c14`](#insn-00aa6c14)

~~~json
{
  "source": "00aa6c14",
  "target": "00c5a4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c20`](#insn-00aa6c20)

~~~json
{
  "source": "00aa6c20",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c2c`](#insn-00aa6c2c)

~~~json
{
  "source": "00aa6c2c",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c30`](#insn-00aa6c30)

~~~json
{
  "source": "00aa6c30",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c34`](#insn-00aa6c34)

~~~json
{
  "source": "00aa6c34",
  "target": "00aa6c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c38`](#insn-00aa6c38)

~~~json
{
  "source": "00aa6c38",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6c3c`](#insn-00aa6c3c)

~~~json
{
  "source": "00aa6c3c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c40`](#insn-00aa6c40)

~~~json
{
  "source": "00aa6c40",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c4c`](#insn-00aa6c4c)

~~~json
{
  "source": "00aa6c4c",
  "target": "002a6e68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6e68",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "426352657347616d61746f746f00",
  "capture_start": "002a6e68",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa6c5c`](#insn-00aa6c5c)

~~~json
{
  "source": "00aa6c5c",
  "target": "0087925c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c68`](#insn-00aa6c68)

~~~json
{
  "source": "00aa6c68",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c78`](#insn-00aa6c78)

~~~json
{
  "source": "00aa6c78",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c84`](#insn-00aa6c84)

~~~json
{
  "source": "00aa6c84",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c94`](#insn-00aa6c94)

~~~json
{
  "source": "00aa6c94",
  "target": "00c5a430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa6c9c`](#insn-00aa6c9c)

~~~json
{
  "source": "00aa6c9c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ca4`](#insn-00aa6ca4)

~~~json
{
  "source": "00aa6ca4",
  "target": "00aa6da0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6ca8`](#insn-00aa6ca8)

~~~json
{
  "source": "00aa6ca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6cac`](#insn-00aa6cac)

~~~json
{
  "source": "00aa6cac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6cb0`](#insn-00aa6cb0)

~~~json
{
  "source": "00aa6cb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6cb4`](#insn-00aa6cb4)

~~~json
{
  "source": "00aa6cb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa6da0`](#insn-00aa6da0)

~~~json
{
  "source": "00aa6da0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
