# 00adae8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adaf54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adaf54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-7986fb37cbd71802d0e4d0d65e568c07)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adae8c",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c10e24787fadc87189ab7a213ba683ab6f8dbdbb813eb60389aa44816589bf22",
  "source_text_sha256": "c10e24787fadc87189ab7a213ba683ab6f8dbdbb813eb60389aa44816589bf22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adae8c",
        "00adaf1b"
      ],
      [
        "00adaf48",
        "00adaf4b"
      ]
    ],
    "bytes_sha256": "6276b7a4ba5fad2afab30fa5c8e357bb3d74c6a0bd0c710b4d082b843c508327",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba18](../00adb/00adba18.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 872 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
                    /* catch() { ... } // from try @ 00adae70 with catch @ 00adae8c */
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba18(&DAT_0109fe50,local_40);
  if ((puVar2 != &DAT_0109fe58) && (plVar3 = (long *)puVar2[0xc], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-00adae8c"></a> `00adae8c` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adae90"></a> `00adae90` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adae94"></a> `00adae94` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adae98"></a> `00adae98` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adae9c"></a> `00adae9c` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adaea0"></a> `00adaea0` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adaea4"></a> `00adaea4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adaea8"></a> `00adaea8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaeac"></a> `00adaeac` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adaeb0"></a> `00adaeb0` | `f3 2e ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adaeb4"></a> `00adaeb4` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaeb8"></a> `00adaeb8` | `00 40 39 91` | add x0,x0,#0xe50 | `FALL_THROUGH`
<a id="insn-00adaebc"></a> `00adaebc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adaec0"></a> `00adaec0` | `d6 02 00 94` | bl 0x00adba18 | `UNCONDITIONAL_CALL`
<a id="insn-00adaec4"></a> `00adaec4` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaec8"></a> `00adaec8` | `08 61 39 91` | add x8,x8,#0xe58 | `FALL_THROUGH`
<a id="insn-00adaecc"></a> `00adaecc` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adaed0"></a> `00adaed0` | `e0 00 00 54` | b.eq 0x00adaeec | `CONDITIONAL_JUMP`
<a id="insn-00adaed4"></a> `00adaed4` | `00 30 40 f9` | ldr x0,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00adaed8"></a> `00adaed8` | `a0 00 00 b4` | cbz x0,0x00adaeec | `CONDITIONAL_JUMP`
<a id="insn-00adaedc"></a> `00adaedc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adaee0"></a> `00adaee0` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adaee4"></a> `00adaee4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adaee8"></a> `00adaee8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adaeec"></a> `00adaeec` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adaef0"></a> `00adaef0` | `68 00 00 36` | tbz w8,#0x0,0x00adaefc | `CONDITIONAL_JUMP`
<a id="insn-00adaef4"></a> `00adaef4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adaef8"></a> `00adaef8` | `1a 00 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adaefc"></a> `00adaefc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adaf00"></a> `00adaf00` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaf04"></a> `00adaf04` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adaf08"></a> `00adaf08` | `01 02 00 54` | b.ne 0x00adaf48 | `CONDITIONAL_JUMP`
<a id="insn-00adaf0c"></a> `00adaf0c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adaf10"></a> `00adaf10` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adaf14"></a> `00adaf14` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adaf18"></a> `00adaf18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adaf48"></a> `00adaf48` | `12 00 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adae8c`](#insn-00adae8c) 範囲 `[['00adae8c', '00adaed3']]`
  - `CONDITIONAL_JUMP` [`00adaed0`](#insn-00adaed0) → [`00adaeec`](#insn-00adaeec)
  - `FALL_THROUGH` [`00adaed0`](#insn-00adaed0) → [`00adaed4`](#insn-00adaed4)
- ブロック [`00adaed4`](#insn-00adaed4) 範囲 `[['00adaed4', '00adaedb']]`
  - `CONDITIONAL_JUMP` [`00adaed8`](#insn-00adaed8) → [`00adaeec`](#insn-00adaeec)
  - `FALL_THROUGH` [`00adaed8`](#insn-00adaed8) → [`00adaedc`](#insn-00adaedc)
- ブロック [`00adaedc`](#insn-00adaedc) 範囲 `[['00adaedc', '00adaeeb']]`
  - `FALL_THROUGH` [`00adaee8`](#insn-00adaee8) → [`00adaeec`](#insn-00adaeec)
- ブロック [`00adaeec`](#insn-00adaeec) 範囲 `[['00adaeec', '00adaef3']]`
  - `CONDITIONAL_JUMP` [`00adaef0`](#insn-00adaef0) → [`00adaefc`](#insn-00adaefc)
  - `FALL_THROUGH` [`00adaef0`](#insn-00adaef0) → [`00adaef4`](#insn-00adaef4)
- ブロック [`00adaef4`](#insn-00adaef4) 範囲 `[['00adaef4', '00adaefb']]`
  - `FALL_THROUGH` [`00adaef8`](#insn-00adaef8) → [`00adaefc`](#insn-00adaefc)
- ブロック [`00adaefc`](#insn-00adaefc) 範囲 `[['00adaefc', '00adaf0b']]`
  - `CONDITIONAL_JUMP` [`00adaf08`](#insn-00adaf08) → [`00adaf48`](#insn-00adaf48)
  - `FALL_THROUGH` [`00adaf08`](#insn-00adaf08) → [`00adaf0c`](#insn-00adaf0c)
- ブロック [`00adaf0c`](#insn-00adaf0c) 範囲 `[['00adaf0c', '00adaf1b']]`
- ブロック [`00adaf48`](#insn-00adaf48) 範囲 `[['00adaf48', '00adaf4b']]`

## 命令位置別の参照

- [`00adae90`](#insn-00adae90) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adae94`](#insn-00adae94) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaea8`](#insn-00adaea8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaeb0`](#insn-00adaeb0) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adaeb8`](#insn-00adaeb8) → `0109fe50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adaec0`](#insn-00adaec0) → [`00adba18`](../00adb/00adba18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adba18` · 推定シンボル `None` · 推定型 `None`
- [`00adaed0`](#insn-00adaed0) → [`00adaeec`](#insn-00adaeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaed8`](#insn-00adaed8) → [`00adaeec`](#insn-00adaeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaeec`](#insn-00adaeec) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaef0`](#insn-00adaef0) → [`00adaefc`](#insn-00adaefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaef4`](#insn-00adaef4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaef8`](#insn-00adaef8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adaf00`](#insn-00adaf00) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf08`](#insn-00adaf08) → [`00adaf48`](#insn-00adaf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf0c`](#insn-00adaf0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf10`](#insn-00adaf10) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf48`](#insn-00adaf48) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adae90`](#insn-00adae90)

~~~json
{
  "source": "00adae90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adae94`](#insn-00adae94)

~~~json
{
  "source": "00adae94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaea8`](#insn-00adaea8)

~~~json
{
  "source": "00adaea8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaeb0`](#insn-00adaeb0)

~~~json
{
  "source": "00adaeb0",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaeb8`](#insn-00adaeb8)

~~~json
{
  "source": "00adaeb8",
  "target": "0109fe50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adaec0`](#insn-00adaec0)

~~~json
{
  "source": "00adaec0",
  "target": "00adba18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaed0`](#insn-00adaed0)

~~~json
{
  "source": "00adaed0",
  "target": "00adaeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaed8`](#insn-00adaed8)

~~~json
{
  "source": "00adaed8",
  "target": "00adaeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaeec`](#insn-00adaeec)

~~~json
{
  "source": "00adaeec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaef0`](#insn-00adaef0)

~~~json
{
  "source": "00adaef0",
  "target": "00adaefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaef4`](#insn-00adaef4)

~~~json
{
  "source": "00adaef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaef8`](#insn-00adaef8)

~~~json
{
  "source": "00adaef8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf00`](#insn-00adaf00)

~~~json
{
  "source": "00adaf00",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf08`](#insn-00adaf08)

~~~json
{
  "source": "00adaf08",
  "target": "00adaf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf0c`](#insn-00adaf0c)

~~~json
{
  "source": "00adaf0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf10`](#insn-00adaf10)

~~~json
{
  "source": "00adaf10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf48`](#insn-00adaf48)

~~~json
{
  "source": "00adaf48",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
