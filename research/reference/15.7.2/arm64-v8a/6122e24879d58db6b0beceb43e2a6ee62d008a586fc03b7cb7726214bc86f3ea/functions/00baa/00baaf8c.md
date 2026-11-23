# 00baaf8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bab054`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab054.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-7162f67b6159e5e41f2d73eaa923dc7e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaf8c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE8do_widenEc",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b66b908968eaaa4169a67308ae0ede514c0387b3e9bedf61bd0215e386f34552",
  "source_text_sha256": "b66b908968eaaa4169a67308ae0ede514c0387b3e9bedf61bd0215e386f34552",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaf8c",
        "00baafe3"
      ]
    ],
    "bytes_sha256": "de845c94c5bf9c11f492afbf375499edb3a8163dd9be49191193e245ff4e5934",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a00](../00be1/00be1a00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 301 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE8do_widenEc(long param_1,uint param_2)

{
  wint_t wVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  wVar1 = btowc(param_2 & 0xff);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  return wVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaf8c"></a> `00baaf8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baaf90"></a> `00baaf90` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baaf94"></a> `00baaf94` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf98"></a> `00baaf98` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf9c"></a> `00baaf9c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baafa0"></a> `00baafa0` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baafa4"></a> `00baafa4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00baafa8"></a> `00baafa8` | `36 d9 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baafac"></a> `00baafac` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baafb0"></a> `00baafb0` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baafb4"></a> `00baafb4` | `80 1e 00 12` | and w0,w20,#0xff | `FALL_THROUGH`
<a id="insn-00baafb8"></a> `00baafb8` | `92 da 00 94` | bl 0x00be1a00 | `UNCONDITIONAL_CALL`
<a id="insn-00baafbc"></a> `00baafbc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00baafc0"></a> `00baafc0` | `73 00 00 b4` | cbz x19,0x00baafcc | `CONDITIONAL_JUMP`
<a id="insn-00baafc4"></a> `00baafc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baafc8"></a> `00baafc8` | `2e d9 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baafcc"></a> `00baafcc` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00baafd0"></a> `00baafd0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baafd4"></a> `00baafd4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baafe0"></a> `00baafe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaf8c`](#insn-00baaf8c) 範囲 `[['00baaf8c', '00baafc3']]`
  - `CONDITIONAL_JUMP` [`00baafc0`](#insn-00baafc0) → [`00baafcc`](#insn-00baafcc)
  - `FALL_THROUGH` [`00baafc0`](#insn-00baafc0) → [`00baafc4`](#insn-00baafc4)
- ブロック [`00baafc4`](#insn-00baafc4) 範囲 `[['00baafc4', '00baafcb']]`
  - `FALL_THROUGH` [`00baafc8`](#insn-00baafc8) → [`00baafcc`](#insn-00baafcc)
- ブロック [`00baafcc`](#insn-00baafcc) 範囲 `[['00baafcc', '00baafe3']]`

## 命令位置別の参照

- [`00baaf94`](#insn-00baaf94) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf98`](#insn-00baaf98) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa8`](#insn-00baafa8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baafb0`](#insn-00baafb0) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb8`](#insn-00baafb8) → [`00be1a00`](../00be1/00be1a00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a00` · 推定シンボル `None` · 推定型 `None`
- [`00baafc0`](#insn-00baafc0) → [`00baafcc`](#insn-00baafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc8`](#insn-00baafc8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baafd0`](#insn-00baafd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafd4`](#insn-00baafd4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaf94`](#insn-00baaf94)

~~~json
{
  "source": "00baaf94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf98`](#insn-00baaf98)

~~~json
{
  "source": "00baaf98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa8`](#insn-00baafa8)

~~~json
{
  "source": "00baafa8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baafb0`](#insn-00baafb0)

~~~json
{
  "source": "00baafb0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb8`](#insn-00baafb8)

~~~json
{
  "source": "00baafb8",
  "target": "00be1a00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baafc0`](#insn-00baafc0)

~~~json
{
  "source": "00baafc0",
  "target": "00baafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc8`](#insn-00baafc8)

~~~json
{
  "source": "00baafc8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baafd0`](#insn-00baafd0)

~~~json
{
  "source": "00baafd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafd4`](#insn-00baafd4)

~~~json
{
  "source": "00baafd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
