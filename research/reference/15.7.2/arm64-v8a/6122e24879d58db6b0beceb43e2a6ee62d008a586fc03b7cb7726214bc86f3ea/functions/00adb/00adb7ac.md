# 00adb7ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adb874`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb874.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-2e8becfcb917148c4e685181819b20c4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb7ac",
  "name": "FUN_00adb7ac",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4538c0d6966673b718d2c05d0ec4af0979a8c9746e21ae15ae824a142608b5e",
  "source_text_sha256": "f4538c0d6966673b718d2c05d0ec4af0979a8c9746e21ae15ae824a142608b5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb7ac",
        "00adb90f"
      ]
    ],
    "bytes_sha256": "3b721b1983d81eceb07c48b7c2fd574fb916b033cb311737f4a06569adfa7e45",
    "instruction_count": 89,
    "instruction_bytes": 356,
    "body_bytes": 356,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

- [00ada4e4](../00ada/00ada4e4.md)
- [00ada6ac](../00ada/00ada6ac.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2581 bytes

~~~c

void FUN_00adb7ac(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long local_60 [5];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (param_2 != param_1) {
    plVar2 = (long *)param_1[4];
    plVar3 = (long *)param_2[4];
    if (plVar2 == param_1) {
      if (plVar3 == param_2) {
        (**(code **)(*param_1 + 0x18))(param_1,local_60);
                    /* catch() { ... } // from try @ 00adb00c with catch @ 00adb884 */
                    /* catch() { ... } // from try @ 00adb254 with catch @ 00adb88c */
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = 0;
                    /* catch() { ... } // from try @ 00adb26c with catch @ 00adb894 */
        (**(code **)(*(long *)param_2[4] + 0x18))((long *)param_2[4],param_1);
        (**(code **)(*(long *)param_2[4] + 0x20))();
                    /* catch() { ... } // from try @ 00adb1d0 with catch @ 00adb8bc */
        param_2[4] = 0;
                    /* catch() { ... } // from try @ 00adb1b0 with catch @ 00adb8c0 */
        param_1[4] = (long)param_1;
                    /* catch() { ... } // from try @ 00adb188 with catch @ 00adb8c4 */
        (**(code **)(local_60[0] + 0x18))(local_60,param_2);
                    /* catch() { ... } // from try @ 00adb65c with catch @ 00adb8dc */
                    /* catch() { ... } // from try @ 00adb4f4 with catch @ 00adb8e0 */
        (**(code **)(local_60[0] + 0x20))(local_60);
      }
      else {
        (**(code **)(*param_1 + 0x18))(param_1,param_2);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = param_2[4];
      }
                    /* catch() { ... } // from try @ 00adb4c0 with catch @ 00adb8e4 */
      param_2[4] = (long)param_2;
    }
    else if (plVar3 == param_2) {
      (**(code **)(*param_2 + 0x18))(param_2,param_1);
      (**(code **)(*(long *)param_2[4] + 0x20))();
      param_2[4] = param_1[4];
      param_1[4] = (long)param_1;
    }
    else {
      param_1[4] = (long)plVar3;
      param_2[4] = (long)plVar2;
    }
  }
                    /* catch() { ... } // from try @ 00adb4b4 with catch @ 00adb8e8 */
                    /* catch() { ... } // from try @ 00adb0c4 with catch @ 00adb8ec */
                    /* catch() { ... } // from try @ 00adb0cc with catch @ 00adb8f4 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00adb0d8 with catch @ 00adb904 */
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
<a id="insn-00adb7ac"></a> `00adb7ac` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adb7b0"></a> `00adb7b0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb7b4"></a> `00adb7b4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb7b8"></a> `00adb7b8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adb7bc"></a> `00adb7bc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adb7c0"></a> `00adb7c0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adb7c4"></a> `00adb7c4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adb7c8"></a> `00adb7c8` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-00adb7cc"></a> `00adb7cc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adb7d0"></a> `00adb7d0` | `c0 08 00 54` | b.eq 0x00adb8e8 | `CONDITIONAL_JUMP`
<a id="insn-00adb7d4"></a> `00adb7d4` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00adb7d8"></a> `00adb7d8` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00adb7dc"></a> `00adb7dc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00adb7e0"></a> `00adb7e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adb7e4"></a> `00adb7e4` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00adb7e8"></a> `00adb7e8` | `c0 00 00 54` | b.eq 0x00adb800 | `CONDITIONAL_JUMP`
<a id="insn-00adb7ec"></a> `00adb7ec` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00adb7f0"></a> `00adb7f0` | `40 02 00 54` | b.eq 0x00adb838 | `CONDITIONAL_JUMP`
<a id="insn-00adb7f4"></a> `00adb7f4` | `89 12 00 f9` | str x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb7f8"></a> `00adb7f8` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb7fc"></a> `00adb7fc` | `3b 00 00 14` | b 0x00adb8e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb800"></a> `00adb800` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00adb804"></a> `00adb804` | `40 03 00 54` | b.eq 0x00adb86c | `CONDITIONAL_JUMP`
<a id="insn-00adb808"></a> `00adb808` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00adb80c"></a> `00adb80c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00adb810"></a> `00adb810` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb814"></a> `00adb814` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adb818"></a> `00adb818` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb81c"></a> `00adb81c` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb820"></a> `00adb820` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adb824"></a> `00adb824` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb828"></a> `00adb828` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb82c"></a> `00adb82c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb830"></a> `00adb830` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb834"></a> `00adb834` | `2c 00 00 14` | b 0x00adb8e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb838"></a> `00adb838` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00adb83c"></a> `00adb83c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00adb840"></a> `00adb840` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adb844"></a> `00adb844` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adb848"></a> `00adb848` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb84c"></a> `00adb84c` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb850"></a> `00adb850` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adb854"></a> `00adb854` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb858"></a> `00adb858` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb85c"></a> `00adb85c` | `88 12 40 f9` | ldr x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb860"></a> `00adb860` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb864"></a> `00adb864` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb868"></a> `00adb868` | `20 00 00 14` | b 0x00adb8e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb86c"></a> `00adb86c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00adb870"></a> `00adb870` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00adb874"></a> `00adb874` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adb878"></a> `00adb878` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb87c"></a> `00adb87c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb880"></a> `00adb880` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb884"></a> `00adb884` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adb888"></a> `00adb888` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb88c"></a> `00adb88c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb890"></a> `00adb890` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb894"></a> `00adb894` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb898"></a> `00adb898` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adb89c"></a> `00adb89c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00adb8a0"></a> `00adb8a0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adb8a4"></a> `00adb8a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb8a8"></a> `00adb8a8` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8ac"></a> `00adb8ac` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adb8b0"></a> `00adb8b0` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8b4"></a> `00adb8b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb8b8"></a> `00adb8b8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00adb8bc"></a> `00adb8bc` | `7f 12 00 f9` | str xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8c0"></a> `00adb8c0` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8c4"></a> `00adb8c4` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00adb8c8"></a> `00adb8c8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00adb8cc"></a> `00adb8cc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00adb8d0"></a> `00adb8d0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb8d4"></a> `00adb8d4` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00adb8d8"></a> `00adb8d8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00adb8dc"></a> `00adb8dc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8e0"></a> `00adb8e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb8e4"></a> `00adb8e4` | `73 12 00 f9` | str x19,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb8e8"></a> `00adb8e8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adb8ec"></a> `00adb8ec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adb8f0"></a> `00adb8f0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adb8f4"></a> `00adb8f4` | `c1 00 00 54` | b.ne 0x00adb90c | `CONDITIONAL_JUMP`
<a id="insn-00adb8f8"></a> `00adb8f8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adb8fc"></a> `00adb8fc` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb900"></a> `00adb900` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb904"></a> `00adb904` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adb908"></a> `00adb908` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adb90c"></a> `00adb90c` | `a1 fd 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb7ac`](#insn-00adb7ac) 範囲 `[['00adb7ac', '00adb7d3']]`
  - `CONDITIONAL_JUMP` [`00adb7d0`](#insn-00adb7d0) → [`00adb8e8`](#insn-00adb8e8)
  - `FALL_THROUGH` [`00adb7d0`](#insn-00adb7d0) → [`00adb7d4`](#insn-00adb7d4)
- ブロック [`00adb7d4`](#insn-00adb7d4) 範囲 `[['00adb7d4', '00adb7eb']]`
  - `CONDITIONAL_JUMP` [`00adb7e8`](#insn-00adb7e8) → [`00adb800`](#insn-00adb800)
  - `FALL_THROUGH` [`00adb7e8`](#insn-00adb7e8) → [`00adb7ec`](#insn-00adb7ec)
- ブロック [`00adb7ec`](#insn-00adb7ec) 範囲 `[['00adb7ec', '00adb7f3']]`
  - `CONDITIONAL_JUMP` [`00adb7f0`](#insn-00adb7f0) → [`00adb838`](#insn-00adb838)
  - `FALL_THROUGH` [`00adb7f0`](#insn-00adb7f0) → [`00adb7f4`](#insn-00adb7f4)
- ブロック [`00adb7f4`](#insn-00adb7f4) 範囲 `[['00adb7f4', '00adb7ff']]`
  - `UNCONDITIONAL_JUMP` [`00adb7fc`](#insn-00adb7fc) → [`00adb8e8`](#insn-00adb8e8)
- ブロック [`00adb800`](#insn-00adb800) 範囲 `[['00adb800', '00adb807']]`
  - `CONDITIONAL_JUMP` [`00adb804`](#insn-00adb804) → [`00adb86c`](#insn-00adb86c)
  - `FALL_THROUGH` [`00adb804`](#insn-00adb804) → [`00adb808`](#insn-00adb808)
- ブロック [`00adb808`](#insn-00adb808) 範囲 `[['00adb808', '00adb837']]`
  - `UNCONDITIONAL_JUMP` [`00adb834`](#insn-00adb834) → [`00adb8e4`](#insn-00adb8e4)
- ブロック [`00adb838`](#insn-00adb838) 範囲 `[['00adb838', '00adb86b']]`
  - `UNCONDITIONAL_JUMP` [`00adb868`](#insn-00adb868) → [`00adb8e8`](#insn-00adb8e8)
- ブロック [`00adb86c`](#insn-00adb86c) 範囲 `[['00adb86c', '00adb883']]`
  - `FALL_THROUGH` [`00adb880`](#insn-00adb880) → [`00adb884`](#insn-00adb884)
- ブロック [`00adb884`](#insn-00adb884) 範囲 `[['00adb884', '00adb88b']]`
  - `FALL_THROUGH` [`00adb888`](#insn-00adb888) → [`00adb88c`](#insn-00adb88c)
- ブロック [`00adb88c`](#insn-00adb88c) 範囲 `[['00adb88c', '00adb893']]`
  - `FALL_THROUGH` [`00adb890`](#insn-00adb890) → [`00adb894`](#insn-00adb894)
- ブロック [`00adb894`](#insn-00adb894) 範囲 `[['00adb894', '00adb8bb']]`
  - `FALL_THROUGH` [`00adb8b8`](#insn-00adb8b8) → [`00adb8bc`](#insn-00adb8bc)
- ブロック [`00adb8bc`](#insn-00adb8bc) 範囲 `[['00adb8bc', '00adb8bf']]`
  - `FALL_THROUGH` [`00adb8bc`](#insn-00adb8bc) → [`00adb8c0`](#insn-00adb8c0)
- ブロック [`00adb8c0`](#insn-00adb8c0) 範囲 `[['00adb8c0', '00adb8c3']]`
  - `FALL_THROUGH` [`00adb8c0`](#insn-00adb8c0) → [`00adb8c4`](#insn-00adb8c4)
- ブロック [`00adb8c4`](#insn-00adb8c4) 範囲 `[['00adb8c4', '00adb8db']]`
  - `FALL_THROUGH` [`00adb8d8`](#insn-00adb8d8) → [`00adb8dc`](#insn-00adb8dc)
- ブロック [`00adb8dc`](#insn-00adb8dc) 範囲 `[['00adb8dc', '00adb8df']]`
  - `FALL_THROUGH` [`00adb8dc`](#insn-00adb8dc) → [`00adb8e0`](#insn-00adb8e0)
- ブロック [`00adb8e0`](#insn-00adb8e0) 範囲 `[['00adb8e0', '00adb8e3']]`
  - `FALL_THROUGH` [`00adb8e0`](#insn-00adb8e0) → [`00adb8e4`](#insn-00adb8e4)
- ブロック [`00adb8e4`](#insn-00adb8e4) 範囲 `[['00adb8e4', '00adb8e7']]`
  - `FALL_THROUGH` [`00adb8e4`](#insn-00adb8e4) → [`00adb8e8`](#insn-00adb8e8)
- ブロック [`00adb8e8`](#insn-00adb8e8) 範囲 `[['00adb8e8', '00adb8eb']]`
  - `FALL_THROUGH` [`00adb8e8`](#insn-00adb8e8) → [`00adb8ec`](#insn-00adb8ec)
- ブロック [`00adb8ec`](#insn-00adb8ec) 範囲 `[['00adb8ec', '00adb8f3']]`
  - `FALL_THROUGH` [`00adb8f0`](#insn-00adb8f0) → [`00adb8f4`](#insn-00adb8f4)
- ブロック [`00adb8f4`](#insn-00adb8f4) 範囲 `[['00adb8f4', '00adb8f7']]`
  - `CONDITIONAL_JUMP` [`00adb8f4`](#insn-00adb8f4) → [`00adb90c`](#insn-00adb90c)
  - `FALL_THROUGH` [`00adb8f4`](#insn-00adb8f4) → [`00adb8f8`](#insn-00adb8f8)
- ブロック [`00adb8f8`](#insn-00adb8f8) 範囲 `[['00adb8f8', '00adb903']]`
  - `FALL_THROUGH` [`00adb900`](#insn-00adb900) → [`00adb904`](#insn-00adb904)
- ブロック [`00adb904`](#insn-00adb904) 範囲 `[['00adb904', '00adb90b']]`
- ブロック [`00adb90c`](#insn-00adb90c) 範囲 `[['00adb90c', '00adb90f']]`

## 命令位置別の参照

- [`00adb7b0`](#insn-00adb7b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7b4`](#insn-00adb7b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7b8`](#insn-00adb7b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7cc`](#insn-00adb7cc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7d0`](#insn-00adb7d0) → [`00adb8e8`](#insn-00adb8e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7e8`](#insn-00adb7e8) → [`00adb800`](#insn-00adb800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7f0`](#insn-00adb7f0) → [`00adb838`](#insn-00adb838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb7fc`](#insn-00adb7fc) → [`00adb8e8`](#insn-00adb8e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb804`](#insn-00adb804) → [`00adb86c`](#insn-00adb86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb834`](#insn-00adb834) → [`00adb8e4`](#insn-00adb8e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb868`](#insn-00adb868) → [`00adb8e8`](#insn-00adb8e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8b8`](#insn-00adb8b8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8d4`](#insn-00adb8d4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8ec`](#insn-00adb8ec) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8f4`](#insn-00adb8f4) → [`00adb90c`](#insn-00adb90c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8f8`](#insn-00adb8f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb8fc`](#insn-00adb8fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb900`](#insn-00adb900) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb90c`](#insn-00adb90c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb7b0`](#insn-00adb7b0)

~~~json
{
  "source": "00adb7b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7b4`](#insn-00adb7b4)

~~~json
{
  "source": "00adb7b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7b8`](#insn-00adb7b8)

~~~json
{
  "source": "00adb7b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7cc`](#insn-00adb7cc)

~~~json
{
  "source": "00adb7cc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7d0`](#insn-00adb7d0)

~~~json
{
  "source": "00adb7d0",
  "target": "00adb8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7e8`](#insn-00adb7e8)

~~~json
{
  "source": "00adb7e8",
  "target": "00adb800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7f0`](#insn-00adb7f0)

~~~json
{
  "source": "00adb7f0",
  "target": "00adb838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb7fc`](#insn-00adb7fc)

~~~json
{
  "source": "00adb7fc",
  "target": "00adb8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb804`](#insn-00adb804)

~~~json
{
  "source": "00adb804",
  "target": "00adb86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb834`](#insn-00adb834)

~~~json
{
  "source": "00adb834",
  "target": "00adb8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb868`](#insn-00adb868)

~~~json
{
  "source": "00adb868",
  "target": "00adb8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8b8`](#insn-00adb8b8)

~~~json
{
  "source": "00adb8b8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8d4`](#insn-00adb8d4)

~~~json
{
  "source": "00adb8d4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8ec`](#insn-00adb8ec)

~~~json
{
  "source": "00adb8ec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8f4`](#insn-00adb8f4)

~~~json
{
  "source": "00adb8f4",
  "target": "00adb90c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8f8`](#insn-00adb8f8)

~~~json
{
  "source": "00adb8f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb8fc`](#insn-00adb8fc)

~~~json
{
  "source": "00adb8fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb900`](#insn-00adb900)

~~~json
{
  "source": "00adb900",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb90c`](#insn-00adb90c)

~~~json
{
  "source": "00adb90c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
