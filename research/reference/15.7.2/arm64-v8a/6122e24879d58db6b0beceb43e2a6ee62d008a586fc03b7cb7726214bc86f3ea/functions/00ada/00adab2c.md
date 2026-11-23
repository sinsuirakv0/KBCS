# 00adab2c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adabf4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adabf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-e62b86351db585331f253732675edd9a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adab2c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ea7b608b3dff791e063c3e8a577b27e949d0d472f7a01a8c310b64e21e1ca71",
  "source_text_sha256": "9ea7b608b3dff791e063c3e8a577b27e949d0d472f7a01a8c310b64e21e1ca71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adab2c",
        "00adabcf"
      ],
      [
        "00adabfc",
        "00adabff"
      ]
    ],
    "bytes_sha256": "d8cb4d0d1747ce9b0fb1be49efec58320dd42a1b7fb0c3303fbae703581e575c",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
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

## 疑似コード / UTF-8 1145 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  undefined4 local_3c;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fef0 != (long *)0x0) {
    FUN_00566a7c(local_58,param_1,param_3);
    local_3c = param_4;
    if (DAT_0109fef0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00adabfc;
    }
                    /* try { // try from 00adab78 to 00bdaba7 has its CatchHandler @ 00adac9c */
    (**(code **)(*DAT_0109fef0 + 0x30))(DAT_0109fef0,local_58,&local_3c);
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00adaba8 to 00bdabdb has its CatchHandler @ 00adaa10 */
    return;
  }
LAB_00adabfc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adab2c"></a> `00adab2c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adab30"></a> `00adab30` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adab34"></a> `00adab34` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adab38"></a> `00adab38` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adab3c"></a> `00adab3c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adab40"></a> `00adab40` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adab44"></a> `00adab44` | `35 2e 00 b0` | adrp x21,0x109f000 | `FALL_THROUGH`
<a id="insn-00adab48"></a> `00adab48` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adab4c"></a> `00adab4c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adab50"></a> `00adab50` | `a8 7a 47 f9` | ldr x8,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00adab54"></a> `00adab54` | `28 02 00 b4` | cbz x8,0x00adab98 | `CONDITIONAL_JUMP`
<a id="insn-00adab58"></a> `00adab58` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adab5c"></a> `00adab5c` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adab60"></a> `00adab60` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00adab64"></a> `00adab64` | `c6 2f ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adab68"></a> `00adab68` | `a0 7a 47 f9` | ldr x0,[x21, #0xef0] | `FALL_THROUGH`
<a id="insn-00adab6c"></a> `00adab6c` | `b3 43 1f b8` | stur w19,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00adab70"></a> `00adab70` | `60 02 00 b4` | cbz x0,0x00adabbc | `CONDITIONAL_JUMP`
<a id="insn-00adab74"></a> `00adab74` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adab78"></a> `00adab78` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adab7c"></a> `00adab7c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adab80"></a> `00adab80` | `a2 33 00 d1` | sub x2,x29,#0xc | `FALL_THROUGH`
<a id="insn-00adab84"></a> `00adab84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adab88"></a> `00adab88` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adab8c"></a> `00adab8c` | `68 00 00 36` | tbz w8,#0x0,0x00adab98 | `CONDITIONAL_JUMP`
<a id="insn-00adab90"></a> `00adab90` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adab94"></a> `00adab94` | `f3 00 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adab98"></a> `00adab98` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adab9c"></a> `00adab9c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaba0"></a> `00adaba0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adaba4"></a> `00adaba4` | `c1 02 00 54` | b.ne 0x00adabfc | `CONDITIONAL_JUMP`
<a id="insn-00adaba8"></a> `00adaba8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adabac"></a> `00adabac` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adabb0"></a> `00adabb0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adabb4"></a> `00adabb4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adabb8"></a> `00adabb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adabbc"></a> `00adabbc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adabc0"></a> `00adabc0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adabc4"></a> `00adabc4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adabc8"></a> `00adabc8` | `a1 01 00 54` | b.ne 0x00adabfc | `CONDITIONAL_JUMP`
<a id="insn-00adabcc"></a> `00adabcc` | `b4 70 e5 97` | bl 0x00436e9c | `CALL_TERMINATOR`
<a id="insn-00adabfc"></a> `00adabfc` | `e5 00 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adab2c`](#insn-00adab2c) 範囲 `[['00adab2c', '00adab57']]`
  - `CONDITIONAL_JUMP` [`00adab54`](#insn-00adab54) → [`00adab98`](#insn-00adab98)
  - `FALL_THROUGH` [`00adab54`](#insn-00adab54) → [`00adab58`](#insn-00adab58)
- ブロック [`00adab58`](#insn-00adab58) 範囲 `[['00adab58', '00adab73']]`
  - `CONDITIONAL_JUMP` [`00adab70`](#insn-00adab70) → [`00adabbc`](#insn-00adabbc)
  - `FALL_THROUGH` [`00adab70`](#insn-00adab70) → [`00adab74`](#insn-00adab74)
- ブロック [`00adab74`](#insn-00adab74) 範囲 `[['00adab74', '00adab77']]`
  - `FALL_THROUGH` [`00adab74`](#insn-00adab74) → [`00adab78`](#insn-00adab78)
- ブロック [`00adab78`](#insn-00adab78) 範囲 `[['00adab78', '00adab8f']]`
  - `CONDITIONAL_JUMP` [`00adab8c`](#insn-00adab8c) → [`00adab98`](#insn-00adab98)
  - `FALL_THROUGH` [`00adab8c`](#insn-00adab8c) → [`00adab90`](#insn-00adab90)
- ブロック [`00adab90`](#insn-00adab90) 範囲 `[['00adab90', '00adab97']]`
  - `FALL_THROUGH` [`00adab94`](#insn-00adab94) → [`00adab98`](#insn-00adab98)
- ブロック [`00adab98`](#insn-00adab98) 範囲 `[['00adab98', '00adaba7']]`
  - `CONDITIONAL_JUMP` [`00adaba4`](#insn-00adaba4) → [`00adabfc`](#insn-00adabfc)
  - `FALL_THROUGH` [`00adaba4`](#insn-00adaba4) → [`00adaba8`](#insn-00adaba8)
- ブロック [`00adaba8`](#insn-00adaba8) 範囲 `[['00adaba8', '00adabbb']]`
- ブロック [`00adabbc`](#insn-00adabbc) 範囲 `[['00adabbc', '00adabcb']]`
  - `CONDITIONAL_JUMP` [`00adabc8`](#insn-00adabc8) → [`00adabfc`](#insn-00adabfc)
  - `FALL_THROUGH` [`00adabc8`](#insn-00adabc8) → [`00adabcc`](#insn-00adabcc)
- ブロック [`00adabcc`](#insn-00adabcc) 範囲 `[['00adabcc', '00adabcf']]`
- ブロック [`00adabfc`](#insn-00adabfc) 範囲 `[['00adabfc', '00adabff']]`

## 命令位置別の参照

- [`00adab30`](#insn-00adab30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab34`](#insn-00adab34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab38`](#insn-00adab38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab4c`](#insn-00adab4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab50`](#insn-00adab50) → `0109fef0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adab54`](#insn-00adab54) → [`00adab98`](#insn-00adab98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab64`](#insn-00adab64) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adab68`](#insn-00adab68) → `0109fef0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adab6c`](#insn-00adab6c) → `Stack[-0x3c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab70`](#insn-00adab70) → [`00adabbc`](#insn-00adabbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab88`](#insn-00adab88) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab8c`](#insn-00adab8c) → [`00adab98`](#insn-00adab98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab90`](#insn-00adab90) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adab94`](#insn-00adab94) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adab9c`](#insn-00adab9c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaba4`](#insn-00adaba4) → [`00adabfc`](#insn-00adabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaba8`](#insn-00adaba8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabac`](#insn-00adabac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabb0`](#insn-00adabb0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabc0`](#insn-00adabc0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabc8`](#insn-00adabc8) → [`00adabfc`](#insn-00adabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adabcc`](#insn-00adabcc) → [`00436e9c`](../00436/00436e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00436e9c` · 推定シンボル `None` · 推定型 `None`
- [`00adabfc`](#insn-00adabfc) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adab30`](#insn-00adab30)

~~~json
{
  "source": "00adab30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab34`](#insn-00adab34)

~~~json
{
  "source": "00adab34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab38`](#insn-00adab38)

~~~json
{
  "source": "00adab38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab4c`](#insn-00adab4c)

~~~json
{
  "source": "00adab4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab50`](#insn-00adab50)

~~~json
{
  "source": "00adab50",
  "target": "0109fef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adab54`](#insn-00adab54)

~~~json
{
  "source": "00adab54",
  "target": "00adab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab64`](#insn-00adab64)

~~~json
{
  "source": "00adab64",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adab68`](#insn-00adab68)

~~~json
{
  "source": "00adab68",
  "target": "0109fef0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fef0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adab6c`](#insn-00adab6c)

~~~json
{
  "source": "00adab6c",
  "target": "Stack[-0x3c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab70`](#insn-00adab70)

~~~json
{
  "source": "00adab70",
  "target": "00adabbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab88`](#insn-00adab88)

~~~json
{
  "source": "00adab88",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab8c`](#insn-00adab8c)

~~~json
{
  "source": "00adab8c",
  "target": "00adab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab90`](#insn-00adab90)

~~~json
{
  "source": "00adab90",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adab94`](#insn-00adab94)

~~~json
{
  "source": "00adab94",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adab9c`](#insn-00adab9c)

~~~json
{
  "source": "00adab9c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaba4`](#insn-00adaba4)

~~~json
{
  "source": "00adaba4",
  "target": "00adabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaba8`](#insn-00adaba8)

~~~json
{
  "source": "00adaba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabac`](#insn-00adabac)

~~~json
{
  "source": "00adabac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabb0`](#insn-00adabb0)

~~~json
{
  "source": "00adabb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabc0`](#insn-00adabc0)

~~~json
{
  "source": "00adabc0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabc8`](#insn-00adabc8)

~~~json
{
  "source": "00adabc8",
  "target": "00adabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adabcc`](#insn-00adabcc)

~~~json
{
  "source": "00adabcc",
  "target": "00436e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adabfc`](#insn-00adabfc)

~~~json
{
  "source": "00adabfc",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
