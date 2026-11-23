# 00ad8cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad8db4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8db4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-9e9b1c4ebd87c627be33eb86a7fe28cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad8cec",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f1f7f461c14eb610c983f6f92f52f7344a5b7181ee61e8e10f4978a1ed3290a0",
  "source_text_sha256": "f1f7f461c14eb610c983f6f92f52f7344a5b7181ee61e8e10f4978a1ed3290a0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad8cec",
        "00ad8d9b"
      ],
      [
        "00ad8dc8",
        "00ad8dcb"
      ]
    ],
    "bytes_sha256": "96080c3e09c83adb69c24b7fbfff8e75eed24e36a518fcde2eb1c69b76305070",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1800 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdRewarded
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  byte local_58;
  undefined1 auStack_57 [15];
  undefined1 *local_48;
  undefined1 *local_40;
  long local_38;
  
                    /* catch() { ... } // from try @ 00ad8c38 with catch @ 00ad8cf4
                       catch() { ... } // from try @ 00ad8ce8 with catch @ 00ad8cf4
                       try { // try from 00ad8cf4 to 00bd8d27 has its CatchHandler @ 00ad8a6c */
                    /* catch() { ... } // from try @ 00ad8bd4 with catch @ 00ad8cf8
                       catch() { ... } // from try @ 00ad8ccc with catch @ 00ad8cf8 */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fdb0 != (long *)0x0) {
    FUN_00566a7c(&local_58,param_1,param_3);
                    /* try { // try from 00ad8d28 to 00bd8e8f has its CatchHandler @ 00ad8d28
                       catch() { ... } // from try @ 00ad8d28 with catch @ 00ad8d28
                       catch() { ... } // from try @ 00ad8ec0 with catch @ 00ad8d28
                       catch() { ... } // from try @ 00ad8fb0 with catch @ 00ad8d28 */
    local_40 = local_48;
    if ((local_58 & 1) == 0) {
      local_40 = auStack_57;
    }
    if (DAT_0109fdb0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8dc8;
    }
    (**(code **)(*DAT_0109fdb0 + 0x30))(DAT_0109fdb0,&local_40);
    if ((local_58 & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8dc8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad8cec"></a> `00ad8cec` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad8cf0"></a> `00ad8cf0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8cf4"></a> `00ad8cf4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad8cf8"></a> `00ad8cf8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad8cfc"></a> `00ad8cfc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad8d00"></a> `00ad8d00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad8d04"></a> `00ad8d04` | `33 2e 00 f0` | adrp x19,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad8d08"></a> `00ad8d08` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8d0c"></a> `00ad8d0c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8d10"></a> `00ad8d10` | `68 da 46 f9` | ldr x8,[x19, #0xdb0] | `FALL_THROUGH`
<a id="insn-00ad8d14"></a> `00ad8d14` | `88 02 00 b4` | cbz x8,0x00ad8d64 | `CONDITIONAL_JUMP`
<a id="insn-00ad8d18"></a> `00ad8d18` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8d1c"></a> `00ad8d1c` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00ad8d20"></a> `00ad8d20` | `f5 23 00 91` | add x21,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8d24"></a> `00ad8d24` | `56 37 ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00ad8d28"></a> `00ad8d28` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8d2c"></a> `00ad8d2c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8d30"></a> `00ad8d30` | `60 da 46 f9` | ldr x0,[x19, #0xdb0] | `FALL_THROUGH`
<a id="insn-00ad8d34"></a> `00ad8d34` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad8d38"></a> `00ad8d38` | `28 15 95 9a` | csinc x8,x9,x21,ne | `FALL_THROUGH`
<a id="insn-00ad8d3c"></a> `00ad8d3c` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad8d40"></a> `00ad8d40` | `40 02 00 b4` | cbz x0,0x00ad8d88 | `CONDITIONAL_JUMP`
<a id="insn-00ad8d44"></a> `00ad8d44` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad8d48"></a> `00ad8d48` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8d4c"></a> `00ad8d4c` | `a1 43 00 d1` | sub x1,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00ad8d50"></a> `00ad8d50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8d54"></a> `00ad8d54` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8d58"></a> `00ad8d58` | `68 00 00 36` | tbz w8,#0x0,0x00ad8d64 | `CONDITIONAL_JUMP`
<a id="insn-00ad8d5c"></a> `00ad8d5c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8d60"></a> `00ad8d60` | `80 08 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8d64"></a> `00ad8d64` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8d68"></a> `00ad8d68` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8d6c"></a> `00ad8d6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8d70"></a> `00ad8d70` | `c1 02 00 54` | b.ne 0x00ad8dc8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8d74"></a> `00ad8d74` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad8d78"></a> `00ad8d78` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad8d7c"></a> `00ad8d7c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8d80"></a> `00ad8d80` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad8d84"></a> `00ad8d84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad8d88"></a> `00ad8d88` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8d8c"></a> `00ad8d8c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8d90"></a> `00ad8d90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8d94"></a> `00ad8d94` | `a1 01 00 54` | b.ne 0x00ad8dc8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8d98"></a> `00ad8d98` | `41 78 e5 97` | bl 0x00436e9c | `CALL_TERMINATOR`
<a id="insn-00ad8dc8"></a> `00ad8dc8` | `72 08 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad8cec`](#insn-00ad8cec) 範囲 `[['00ad8cec', '00ad8cf3']]`
  - `FALL_THROUGH` [`00ad8cf0`](#insn-00ad8cf0) → [`00ad8cf4`](#insn-00ad8cf4)
- ブロック [`00ad8cf4`](#insn-00ad8cf4) 範囲 `[['00ad8cf4', '00ad8cf7']]`
  - `FALL_THROUGH` [`00ad8cf4`](#insn-00ad8cf4) → [`00ad8cf8`](#insn-00ad8cf8)
- ブロック [`00ad8cf8`](#insn-00ad8cf8) 範囲 `[['00ad8cf8', '00ad8d17']]`
  - `CONDITIONAL_JUMP` [`00ad8d14`](#insn-00ad8d14) → [`00ad8d64`](#insn-00ad8d64)
  - `FALL_THROUGH` [`00ad8d14`](#insn-00ad8d14) → [`00ad8d18`](#insn-00ad8d18)
- ブロック [`00ad8d18`](#insn-00ad8d18) 範囲 `[['00ad8d18', '00ad8d27']]`
  - `FALL_THROUGH` [`00ad8d24`](#insn-00ad8d24) → [`00ad8d28`](#insn-00ad8d28)
- ブロック [`00ad8d28`](#insn-00ad8d28) 範囲 `[['00ad8d28', '00ad8d43']]`
  - `CONDITIONAL_JUMP` [`00ad8d40`](#insn-00ad8d40) → [`00ad8d88`](#insn-00ad8d88)
  - `FALL_THROUGH` [`00ad8d40`](#insn-00ad8d40) → [`00ad8d44`](#insn-00ad8d44)
- ブロック [`00ad8d44`](#insn-00ad8d44) 範囲 `[['00ad8d44', '00ad8d5b']]`
  - `CONDITIONAL_JUMP` [`00ad8d58`](#insn-00ad8d58) → [`00ad8d64`](#insn-00ad8d64)
  - `FALL_THROUGH` [`00ad8d58`](#insn-00ad8d58) → [`00ad8d5c`](#insn-00ad8d5c)
- ブロック [`00ad8d5c`](#insn-00ad8d5c) 範囲 `[['00ad8d5c', '00ad8d63']]`
  - `FALL_THROUGH` [`00ad8d60`](#insn-00ad8d60) → [`00ad8d64`](#insn-00ad8d64)
- ブロック [`00ad8d64`](#insn-00ad8d64) 範囲 `[['00ad8d64', '00ad8d73']]`
  - `CONDITIONAL_JUMP` [`00ad8d70`](#insn-00ad8d70) → [`00ad8dc8`](#insn-00ad8dc8)
  - `FALL_THROUGH` [`00ad8d70`](#insn-00ad8d70) → [`00ad8d74`](#insn-00ad8d74)
- ブロック [`00ad8d74`](#insn-00ad8d74) 範囲 `[['00ad8d74', '00ad8d87']]`
- ブロック [`00ad8d88`](#insn-00ad8d88) 範囲 `[['00ad8d88', '00ad8d97']]`
  - `CONDITIONAL_JUMP` [`00ad8d94`](#insn-00ad8d94) → [`00ad8dc8`](#insn-00ad8dc8)
  - `FALL_THROUGH` [`00ad8d94`](#insn-00ad8d94) → [`00ad8d98`](#insn-00ad8d98)
- ブロック [`00ad8d98`](#insn-00ad8d98) 範囲 `[['00ad8d98', '00ad8d9b']]`
- ブロック [`00ad8dc8`](#insn-00ad8dc8) 範囲 `[['00ad8dc8', '00ad8dcb']]`

## 命令位置別の参照

- [`00ad8cf0`](#insn-00ad8cf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8cf4`](#insn-00ad8cf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8cf8`](#insn-00ad8cf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d0c`](#insn-00ad8d0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d10`](#insn-00ad8d10) → `0109fdb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8d14`](#insn-00ad8d14) → [`00ad8d64`](#insn-00ad8d64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d24`](#insn-00ad8d24) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d28`](#insn-00ad8d28) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d2c`](#insn-00ad8d2c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d30`](#insn-00ad8d30) → `0109fdb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8d3c`](#insn-00ad8d3c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d40`](#insn-00ad8d40) → [`00ad8d88`](#insn-00ad8d88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d54`](#insn-00ad8d54) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d58`](#insn-00ad8d58) → [`00ad8d64`](#insn-00ad8d64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d5c`](#insn-00ad8d5c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d60`](#insn-00ad8d60) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d68`](#insn-00ad8d68) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d70`](#insn-00ad8d70) → [`00ad8dc8`](#insn-00ad8dc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d74`](#insn-00ad8d74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d78`](#insn-00ad8d78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d7c`](#insn-00ad8d7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d8c`](#insn-00ad8d8c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d94`](#insn-00ad8d94) → [`00ad8dc8`](#insn-00ad8dc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8d98`](#insn-00ad8d98) → [`00436e9c`](../00436/00436e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00436e9c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8dc8`](#insn-00ad8dc8) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad8cf0`](#insn-00ad8cf0)

~~~json
{
  "source": "00ad8cf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8cf4`](#insn-00ad8cf4)

~~~json
{
  "source": "00ad8cf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8cf8`](#insn-00ad8cf8)

~~~json
{
  "source": "00ad8cf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d0c`](#insn-00ad8d0c)

~~~json
{
  "source": "00ad8d0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d10`](#insn-00ad8d10)

~~~json
{
  "source": "00ad8d10",
  "target": "0109fdb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fdb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8d14`](#insn-00ad8d14)

~~~json
{
  "source": "00ad8d14",
  "target": "00ad8d64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d24`](#insn-00ad8d24)

~~~json
{
  "source": "00ad8d24",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8d28`](#insn-00ad8d28)

~~~json
{
  "source": "00ad8d28",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d2c`](#insn-00ad8d2c)

~~~json
{
  "source": "00ad8d2c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d30`](#insn-00ad8d30)

~~~json
{
  "source": "00ad8d30",
  "target": "0109fdb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fdb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8d3c`](#insn-00ad8d3c)

~~~json
{
  "source": "00ad8d3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d40`](#insn-00ad8d40)

~~~json
{
  "source": "00ad8d40",
  "target": "00ad8d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d54`](#insn-00ad8d54)

~~~json
{
  "source": "00ad8d54",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d58`](#insn-00ad8d58)

~~~json
{
  "source": "00ad8d58",
  "target": "00ad8d64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d5c`](#insn-00ad8d5c)

~~~json
{
  "source": "00ad8d5c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d60`](#insn-00ad8d60)

~~~json
{
  "source": "00ad8d60",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8d68`](#insn-00ad8d68)

~~~json
{
  "source": "00ad8d68",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d70`](#insn-00ad8d70)

~~~json
{
  "source": "00ad8d70",
  "target": "00ad8dc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d74`](#insn-00ad8d74)

~~~json
{
  "source": "00ad8d74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d78`](#insn-00ad8d78)

~~~json
{
  "source": "00ad8d78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d7c`](#insn-00ad8d7c)

~~~json
{
  "source": "00ad8d7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d8c`](#insn-00ad8d8c)

~~~json
{
  "source": "00ad8d8c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d94`](#insn-00ad8d94)

~~~json
{
  "source": "00ad8d94",
  "target": "00ad8dc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8d98`](#insn-00ad8d98)

~~~json
{
  "source": "00ad8d98",
  "target": "00436e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8dc8`](#insn-00ad8dc8)

~~~json
{
  "source": "00ad8dc8",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
