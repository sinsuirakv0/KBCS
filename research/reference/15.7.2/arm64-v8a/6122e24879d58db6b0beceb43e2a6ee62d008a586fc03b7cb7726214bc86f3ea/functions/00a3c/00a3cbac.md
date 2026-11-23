# 00a3cbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a3cbac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0040.md#compare-1a49559c2b3a9efd0e39c69df929bd7f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3cbac",
  "name": "FUN_00a3cbac",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5169c35275898f76d193e5948903f9b3febef997489273c4f2e3041e4e29f32",
  "source_text_sha256": "c5169c35275898f76d193e5948903f9b3febef997489273c4f2e3041e4e29f32",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3cbac",
        "00a3cc27"
      ]
    ],
    "bytes_sha256": "bcde41ea3069d7fe11013a6827e68d4cb632a37addccd5bd1ccb2d33b0f6721e",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0073ab94](../0073a/0073ab94.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 574 bytes

~~~c

void FUN_00a3cbac(void)

{
  long lVar1;
  long lVar2;
  byte local_40 [8];
  ulong local_38;
  void *pvStack_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_0081f580();
  FUN_0073ab94(local_40);
  if ((local_40[0] & 1) == 0) {
    local_38 = (ulong)(local_40[0] >> 1);
  }
  else {
    _ZdlPv(pvStack_30);
  }
  lVar2 = FUN_0081f580();
  *(bool *)(lVar2 + 0x4494ea) = local_38 == 0;
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
<a id="insn-00a3cbac"></a> `00a3cbac` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00a3cbb0"></a> `00a3cbb0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3cbb4"></a> `00a3cbb4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3cbb8"></a> `00a3cbb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a3cbbc"></a> `00a3cbbc` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a3cbc0"></a> `00a3cbc0` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a3cbc4"></a> `00a3cbc4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3cbc8"></a> `00a3cbc8` | `6e 8a f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cbcc"></a> `00a3cbcc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a3cbd0"></a> `00a3cbd0` | `f1 f7 f3 97` | bl 0x0073ab94 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cbd4"></a> `00a3cbd4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a3cbd8"></a> `00a3cbd8` | `68 00 00 37` | tbnz w8,#0x0,0x00a3cbe4 | `CONDITIONAL_JUMP`
<a id="insn-00a3cbdc"></a> `00a3cbdc` | `14 fd 41 d3` | lsr x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a3cbe0"></a> `00a3cbe0` | `03 00 00 14` | b 0x00a3cbec | `UNCONDITIONAL_JUMP`
<a id="insn-00a3cbe4"></a> `00a3cbe4` | `f4 83 40 a9` | ldp x20,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a3cbe8"></a> `00a3cbe8` | `de 78 06 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cbec"></a> `00a3cbec` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00a3cbf0"></a> `00a3cbf0` | `f4 17 9f 1a` | cset w20,eq | `FALL_THROUGH`
<a id="insn-00a3cbf4"></a> `00a3cbf4` | `63 8a f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a3cbf8"></a> `00a3cbf8` | `48 9d 92 52` | mov w8,#0x94ea | `FALL_THROUGH`
<a id="insn-00a3cbfc"></a> `00a3cbfc` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-00a3cc00"></a> `00a3cc00` | `14 68 28 38` | strb w20,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a3cc04"></a> `00a3cc04` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a3cc08"></a> `00a3cc08` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a3cc0c"></a> `00a3cc0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a3cc10"></a> `00a3cc10` | `a1 00 00 54` | b.ne 0x00a3cc24 | `CONDITIONAL_JUMP`
<a id="insn-00a3cc14"></a> `00a3cc14` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3cc18"></a> `00a3cc18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3cc1c"></a> `00a3cc1c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00a3cc20"></a> `00a3cc20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a3cc24"></a> `00a3cc24` | `db 78 06 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3cbac`](#insn-00a3cbac) 範囲 `[['00a3cbac', '00a3cbdb']]`
  - `CONDITIONAL_JUMP` [`00a3cbd8`](#insn-00a3cbd8) → [`00a3cbe4`](#insn-00a3cbe4)
  - `FALL_THROUGH` [`00a3cbd8`](#insn-00a3cbd8) → [`00a3cbdc`](#insn-00a3cbdc)
- ブロック [`00a3cbdc`](#insn-00a3cbdc) 範囲 `[['00a3cbdc', '00a3cbe3']]`
  - `UNCONDITIONAL_JUMP` [`00a3cbe0`](#insn-00a3cbe0) → [`00a3cbec`](#insn-00a3cbec)
- ブロック [`00a3cbe4`](#insn-00a3cbe4) 範囲 `[['00a3cbe4', '00a3cbeb']]`
  - `FALL_THROUGH` [`00a3cbe8`](#insn-00a3cbe8) → [`00a3cbec`](#insn-00a3cbec)
- ブロック [`00a3cbec`](#insn-00a3cbec) 範囲 `[['00a3cbec', '00a3cc13']]`
  - `CONDITIONAL_JUMP` [`00a3cc10`](#insn-00a3cc10) → [`00a3cc24`](#insn-00a3cc24)
  - `FALL_THROUGH` [`00a3cc10`](#insn-00a3cc10) → [`00a3cc14`](#insn-00a3cc14)
- ブロック [`00a3cc14`](#insn-00a3cc14) 範囲 `[['00a3cc14', '00a3cc23']]`
- ブロック [`00a3cc24`](#insn-00a3cc24) 範囲 `[['00a3cc24', '00a3cc27']]`

## 命令位置別の参照

- [`00a3cbb0`](#insn-00a3cbb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbb4`](#insn-00a3cbb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbc4`](#insn-00a3cbc4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbc8`](#insn-00a3cbc8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbd0`](#insn-00a3cbd0) → [`0073ab94`](../0073a/0073ab94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0073ab94` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbd4`](#insn-00a3cbd4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbd8`](#insn-00a3cbd8) → [`00a3cbe4`](#insn-00a3cbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbe0`](#insn-00a3cbe0) → [`00a3cbec`](#insn-00a3cbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbe4`](#insn-00a3cbe4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbe8`](#insn-00a3cbe8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00a3cbf4`](#insn-00a3cbf4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a3cc08`](#insn-00a3cc08) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cc10`](#insn-00a3cc10) → [`00a3cc24`](#insn-00a3cc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cc14`](#insn-00a3cc14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cc18`](#insn-00a3cc18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3cc24`](#insn-00a3cc24) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3cbb0`](#insn-00a3cbb0)

~~~json
{
  "source": "00a3cbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbb4`](#insn-00a3cbb4)

~~~json
{
  "source": "00a3cbb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbc4`](#insn-00a3cbc4)

~~~json
{
  "source": "00a3cbc4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbc8`](#insn-00a3cbc8)

~~~json
{
  "source": "00a3cbc8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cbd0`](#insn-00a3cbd0)

~~~json
{
  "source": "00a3cbd0",
  "target": "0073ab94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cbd4`](#insn-00a3cbd4)

~~~json
{
  "source": "00a3cbd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbd8`](#insn-00a3cbd8)

~~~json
{
  "source": "00a3cbd8",
  "target": "00a3cbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbe0`](#insn-00a3cbe0)

~~~json
{
  "source": "00a3cbe0",
  "target": "00a3cbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbe4`](#insn-00a3cbe4)

~~~json
{
  "source": "00a3cbe4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cbe8`](#insn-00a3cbe8)

~~~json
{
  "source": "00a3cbe8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cbf4`](#insn-00a3cbf4)

~~~json
{
  "source": "00a3cbf4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3cc08`](#insn-00a3cc08)

~~~json
{
  "source": "00a3cc08",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cc10`](#insn-00a3cc10)

~~~json
{
  "source": "00a3cc10",
  "target": "00a3cc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cc14`](#insn-00a3cc14)

~~~json
{
  "source": "00a3cc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cc18`](#insn-00a3cc18)

~~~json
{
  "source": "00a3cc18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3cc24`](#insn-00a3cc24)

~~~json
{
  "source": "00a3cc24",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
