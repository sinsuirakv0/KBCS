# 00bbbdf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbbebc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbebc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3b1f84eabf155dd64ab9f697c72c793f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbdf4",
  "name": "FUN_00bbbdf4",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df906d4277d9f9902da3146e7f277251c1d44a5e9dc305652ebfb6f1cc582ea7",
  "source_text_sha256": "df906d4277d9f9902da3146e7f277251c1d44a5e9dc305652ebfb6f1cc582ea7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbdf4",
        "00bbbe93"
      ]
    ],
    "bytes_sha256": "752a39d75dbf41f8ceebe066bf08bf9efec05aa39eff30361219e82c31e1d967",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbba44](../00bbb/00bbba44.md)
- [00bbbd00](../00bbb/00bbbd00.md)

## 呼び出し先

- [00bdb6c0](../00bdb/00bdb6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 999 bytes

~~~c

bool FUN_00bbbdf4(long param_1,long param_2)

{
  bool bVar1;
  long lVar2;
  
  if (param_2 != 0) {
                    /* try { // try from 00bbbe2c to 00cbbe33 has its CatchHandler @ 00bbd2c4 */
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bf48,
                           PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1bf80,0);
    bVar1 = false;
    if (lVar2 != 0) {
                    /* try { // try from 00bbbe38 to 00cbbe47 has its CatchHandler @ 00bbd2a8 */
      if (((*(uint *)(lVar2 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) == 0) &&
         (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar2 + 0x18) + 8))) {
        bVar1 = *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar2 + 0x20) + 8);
      }
      else {
                    /* try { // try from 00bbbe5c to 00cbbe63 has its CatchHandler @ 00bbd0e0 */
        bVar1 = false;
      }
    }
    return bVar1;
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbdf4"></a> `00bbbdf4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbbdf8"></a> `00bbbdf8` | `c1 03 00 b4` | cbz x1,0x00bbbe70 | `CONDITIONAL_JUMP`
<a id="insn-00bbbdfc"></a> `00bbbdfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbe00"></a> `00bbbe00` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbbe04"></a> `00bbbe04` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe08"></a> `00bbbe08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbe0c"></a> `00bbbe0c` | `08 03 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbe10"></a> `00bbbe10` | `02 03 00 90` | adrp x2,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbe14"></a> `00bbbe14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbe18"></a> `00bbbe18` | `08 a5 47 f9` | ldr x8,[x8, #0xf48] | `FALL_THROUGH`
<a id="insn-00bbbe1c"></a> `00bbbe1c` | `42 c0 47 f9` | ldr x2,[x2, #0xf80] | `FALL_THROUGH`
<a id="insn-00bbbe20"></a> `00bbbe20` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbbe24"></a> `00bbbe24` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe28"></a> `00bbbe28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bbbe2c"></a> `00bbbe2c` | `25 7e 00 94` | bl 0x00bdb6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe30"></a> `00bbbe30` | `80 01 00 b4` | cbz x0,0x00bbbe60 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe34"></a> `00bbbe34` | `68 12 40 b9` | ldr w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe38"></a> `00bbbe38` | `09 10 40 b9` | ldr w9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe3c"></a> `00bbbe3c` | `3f 01 28 6a` | bics wzr,w9,w8 | `FALL_THROUGH`
<a id="insn-00bbbe40"></a> `00bbbe40` | `e1 00 00 54` | b.ne 0x00bbbe5c | `CONDITIONAL_JUMP`
<a id="insn-00bbbe44"></a> `00bbbe44` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe48"></a> `00bbbe48` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe4c"></a> `00bbbe4c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe50"></a> `00bbbe50` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe54"></a> `00bbbe54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbe58"></a> `00bbbe58` | `00 01 00 54` | b.eq 0x00bbbe78 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe5c"></a> `00bbbe5c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbe60"></a> `00bbbe60` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe64"></a> `00bbbe64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbbe68"></a> `00bbbe68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbe6c"></a> `00bbbe6c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbe70"></a> `00bbbe70` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbe74"></a> `00bbbe74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbe78"></a> `00bbbe78` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbe7c"></a> `00bbbe7c` | `09 10 40 f9` | ldr x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbe80"></a> `00bbbe80` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe84"></a> `00bbbe84` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe88"></a> `00bbbe88` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbe8c"></a> `00bbbe8c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbe90"></a> `00bbbe90` | `f4 ff ff 17` | b 0x00bbbe60 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbdf4`](#insn-00bbbdf4) 範囲 `[['00bbbdf4', '00bbbdfb']]`
  - `CONDITIONAL_JUMP` [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbe70`](#insn-00bbbe70)
  - `FALL_THROUGH` [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbdfc`](#insn-00bbbdfc)
- ブロック [`00bbbdfc`](#insn-00bbbdfc) 範囲 `[['00bbbdfc', '00bbbe2b']]`
  - `FALL_THROUGH` [`00bbbe28`](#insn-00bbbe28) → [`00bbbe2c`](#insn-00bbbe2c)
- ブロック [`00bbbe2c`](#insn-00bbbe2c) 範囲 `[['00bbbe2c', '00bbbe33']]`
  - `CONDITIONAL_JUMP` [`00bbbe30`](#insn-00bbbe30) → [`00bbbe60`](#insn-00bbbe60)
  - `FALL_THROUGH` [`00bbbe30`](#insn-00bbbe30) → [`00bbbe34`](#insn-00bbbe34)
- ブロック [`00bbbe34`](#insn-00bbbe34) 範囲 `[['00bbbe34', '00bbbe37']]`
  - `FALL_THROUGH` [`00bbbe34`](#insn-00bbbe34) → [`00bbbe38`](#insn-00bbbe38)
- ブロック [`00bbbe38`](#insn-00bbbe38) 範囲 `[['00bbbe38', '00bbbe43']]`
  - `CONDITIONAL_JUMP` [`00bbbe40`](#insn-00bbbe40) → [`00bbbe5c`](#insn-00bbbe5c)
  - `FALL_THROUGH` [`00bbbe40`](#insn-00bbbe40) → [`00bbbe44`](#insn-00bbbe44)
- ブロック [`00bbbe44`](#insn-00bbbe44) 範囲 `[['00bbbe44', '00bbbe5b']]`
  - `CONDITIONAL_JUMP` [`00bbbe58`](#insn-00bbbe58) → [`00bbbe78`](#insn-00bbbe78)
  - `FALL_THROUGH` [`00bbbe58`](#insn-00bbbe58) → [`00bbbe5c`](#insn-00bbbe5c)
- ブロック [`00bbbe5c`](#insn-00bbbe5c) 範囲 `[['00bbbe5c', '00bbbe5f']]`
  - `FALL_THROUGH` [`00bbbe5c`](#insn-00bbbe5c) → [`00bbbe60`](#insn-00bbbe60)
- ブロック [`00bbbe60`](#insn-00bbbe60) 範囲 `[['00bbbe60', '00bbbe6f']]`
- ブロック [`00bbbe70`](#insn-00bbbe70) 範囲 `[['00bbbe70', '00bbbe77']]`
- ブロック [`00bbbe78`](#insn-00bbbe78) 範囲 `[['00bbbe78', '00bbbe93']]`
  - `UNCONDITIONAL_JUMP` [`00bbbe90`](#insn-00bbbe90) → [`00bbbe60`](#insn-00bbbe60)

## 命令位置別の参照

- [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbe70`](#insn-00bbbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe00`](#insn-00bbbe00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe04`](#insn-00bbbe04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe18`](#insn-00bbbe18) → `00c1bf48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe1c`](#insn-00bbbe1c) → `00c1bf80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe1c`](#insn-00bbbe1c) → `00c16b88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe28`](#insn-00bbbe28) → `00c16b10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe2c`](#insn-00bbbe2c) → [`00bdb6c0`](../00bdb/00bdb6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe30`](#insn-00bbbe30) → [`00bbbe60`](#insn-00bbbe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe40`](#insn-00bbbe40) → [`00bbbe5c`](#insn-00bbbe5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe58`](#insn-00bbbe58) → [`00bbbe78`](#insn-00bbbe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe60`](#insn-00bbbe60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe64`](#insn-00bbbe64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe90`](#insn-00bbbe90) → [`00bbbe60`](#insn-00bbbe60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbdf8`](#insn-00bbbdf8)

~~~json
{
  "source": "00bbbdf8",
  "target": "00bbbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe00`](#insn-00bbbe00)

~~~json
{
  "source": "00bbbe00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe04`](#insn-00bbbe04)

~~~json
{
  "source": "00bbbe04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe18`](#insn-00bbbe18)

~~~json
{
  "source": "00bbbe18",
  "target": "00c1bf48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe1c`](#insn-00bbbe1c)

~~~json
{
  "source": "00bbbe1c",
  "target": "00c1bf80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe1c`](#insn-00bbbe1c)

~~~json
{
  "source": "00bbbe1c",
  "target": "00c16b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16b88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe28`](#insn-00bbbe28)

~~~json
{
  "source": "00bbbe28",
  "target": "00c16b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16b10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe2c`](#insn-00bbbe2c)

~~~json
{
  "source": "00bbbe2c",
  "target": "00bdb6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe30`](#insn-00bbbe30)

~~~json
{
  "source": "00bbbe30",
  "target": "00bbbe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe40`](#insn-00bbbe40)

~~~json
{
  "source": "00bbbe40",
  "target": "00bbbe5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe58`](#insn-00bbbe58)

~~~json
{
  "source": "00bbbe58",
  "target": "00bbbe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe60`](#insn-00bbbe60)

~~~json
{
  "source": "00bbbe60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe64`](#insn-00bbbe64)

~~~json
{
  "source": "00bbbe64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe90`](#insn-00bbbe90)

~~~json
{
  "source": "00bbbe90",
  "target": "00bbbe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
