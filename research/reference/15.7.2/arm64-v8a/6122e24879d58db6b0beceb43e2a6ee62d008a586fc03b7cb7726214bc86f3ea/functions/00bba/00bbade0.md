# 00bbade0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaea8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-bb98261b804f750f910449dea5e848cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbade0",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b816449440e6d5f68d7d7e458f207e49df2f1504666abb562feeaa7d3bd16150",
  "source_text_sha256": "b816449440e6d5f68d7d7e458f207e49df2f1504666abb562feeaa7d3bd16150",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbade0",
        "00bbae37"
      ]
    ],
    "bytes_sha256": "cfdd09e25b32dd71bd8dc74730a41bbeecc26056cbc62d5e72c488e5079e4972",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdd970](../00bdd/00bdd970.md)
- [00be0e70](../00be0/00be0e70.md)
- [00be0ed0](../00be0/00be0ed0.md)
- [00be10a0](../00be1/00be10a0.md)
- [00be1d80](../00be1/00be1d80.md)

## 呼び出し先

- [00bd6d30](../00bd6/00bd6d30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb390](../00bdb/00bdb390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bb68 + 0x10);
  iVar1 = FUN_00bd6d30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbade0"></a> `00bbade0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbade4"></a> `00bbade4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbade8"></a> `00bbade8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbadec"></a> `00bbadec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbadf0"></a> `00bbadf0` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbadf4"></a> `00bbadf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbadf8"></a> `00bbadf8` | `08 b5 45 f9` | ldr x8,[x8, #0xb68] | `FALL_THROUGH`
<a id="insn-00bbadfc"></a> `00bbadfc` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbae00"></a> `00bbae00` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbae04"></a> `00bbae04` | `81 22 00 d1` | sub x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bbae08"></a> `00bbae08` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbae0c"></a> `00bbae0c` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbae10"></a> `00bbae10` | `c8 6f 00 94` | bl 0x00bd6d30 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae14"></a> `00bbae14` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbae18"></a> `00bbae18` | `65 00 00 54` | b.pl 0x00bbae24 | `CONDITIONAL_JUMP`
<a id="insn-00bbae1c"></a> `00bbae1c` | `80 62 00 d1` | sub x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bbae20"></a> `00bbae20` | `50 80 00 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbae24"></a> `00bbae24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbae28"></a> `00bbae28` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbae2c"></a> `00bbae2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbae30"></a> `00bbae30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbae34"></a> `00bbae34` | `57 81 00 14` | b 0x00bdb390 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbade0`](#insn-00bbade0) 範囲 `[['00bbade0', '00bbae1b']]`
  - `CONDITIONAL_JUMP` [`00bbae18`](#insn-00bbae18) → [`00bbae24`](#insn-00bbae24)
  - `FALL_THROUGH` [`00bbae18`](#insn-00bbae18) → [`00bbae1c`](#insn-00bbae1c)
- ブロック [`00bbae1c`](#insn-00bbae1c) 範囲 `[['00bbae1c', '00bbae23']]`
  - `FALL_THROUGH` [`00bbae20`](#insn-00bbae20) → [`00bbae24`](#insn-00bbae24)
- ブロック [`00bbae24`](#insn-00bbae24) 範囲 `[['00bbae24', '00bbae37']]`

## 命令位置別の参照

- [`00bbade4`](#insn-00bbade4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbade8`](#insn-00bbade8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbadf8`](#insn-00bbadf8) → `00c1bb68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbae08`](#insn-00bbae08) → `00c16858`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00bbae10`](#insn-00bbae10) → [`00bd6d30`](../00bd6/00bd6d30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d30` · 推定シンボル `None` · 推定型 `None`
- [`00bbae18`](#insn-00bbae18) → [`00bbae24`](#insn-00bbae24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae20`](#insn-00bbae20) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00bbae28`](#insn-00bbae28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae2c`](#insn-00bbae2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbae34`](#insn-00bbae34) → [`00bdb390`](../00bdb/00bdb390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb390` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbade4`](#insn-00bbade4)

~~~json
{
  "source": "00bbade4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbade8`](#insn-00bbade8)

~~~json
{
  "source": "00bbade8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbadf8`](#insn-00bbadf8)

~~~json
{
  "source": "00bbadf8",
  "target": "00c1bb68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bb68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbae08`](#insn-00bbae08)

~~~json
{
  "source": "00bbae08",
  "target": "00c16858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16848",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bbae10`](#insn-00bbae10)

~~~json
{
  "source": "00bbae10",
  "target": "00bd6d30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae18`](#insn-00bbae18)

~~~json
{
  "source": "00bbae18",
  "target": "00bbae24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae20`](#insn-00bbae20)

~~~json
{
  "source": "00bbae20",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbae28`](#insn-00bbae28)

~~~json
{
  "source": "00bbae28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae2c`](#insn-00bbae2c)

~~~json
{
  "source": "00bbae2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbae34`](#insn-00bbae34)

~~~json
{
  "source": "00bbae34",
  "target": "00bdb390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
