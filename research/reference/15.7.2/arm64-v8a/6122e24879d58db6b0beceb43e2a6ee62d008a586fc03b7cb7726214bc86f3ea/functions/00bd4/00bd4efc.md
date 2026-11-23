# 00bd4efc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd4fc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-f0b0e8a7ccfb2d1042b2a2a46a423c35)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd4efc",
  "name": "__cxa_allocate_exception",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f6a8fc0cf16473423b27f27e10f92c87596a011e50a3f942e5c678437fbc23c",
  "source_text_sha256": "7f6a8fc0cf16473423b27f27e10f92c87596a011e50a3f942e5c678437fbc23c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd4efc",
        "00bd4f47"
      ]
    ],
    "bytes_sha256": "fc97b53766ee99f4eea6784748b5055408f96e6bba450c48b23fbcca88bbeb18",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdafa0](../00bda/00bdafa0.md)

## 呼び出し先

- [00bd56c8](../00bd5/00bd56c8.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdb140](../00bdb/00bdb140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1272 bytes

~~~c

long __cxa_allocate_exception(long param_1)

{
  void *__s;
  
  __s = (void *)FUN_00bd56c8(param_1 + 0x8fU & 0xfffffffffffffff0);
  if (__s != (void *)0x0) {
                    /* try { // try from 00bd4f2c to 00cd4f67 has its CatchHandler @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4f2c with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4f84 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd4ffc with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd506c with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd50cc with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd50f0 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5178 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5240 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5330 with catch @ 00bd4f2c
                       catch() { ... } // from try @ 00bd5408 with catch @ 00bd4f2c */
    memset(__s,0,param_1 + 0x8fU & 0xfffffffffffffff0);
    return (long)__s + 0x80;
  }
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd4efc"></a> `00bd4efc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd4f00"></a> `00bd4f00` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd4f04"></a> `00bd4f04` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4f08"></a> `00bd4f08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd4f0c"></a> `00bd4f0c` | `14 3c 02 91` | add x20,x0,#0x8f | `FALL_THROUGH`
<a id="insn-00bd4f10"></a> `00bd4f10` | `80 ee 7c 92` | and x0,x20,#-0x10 | `FALL_THROUGH`
<a id="insn-00bd4f14"></a> `00bd4f14` | `ed 01 00 94` | bl 0x00bd56c8 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4f18"></a> `00bd4f18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd4f1c"></a> `00bd4f1c` | `40 01 00 b4` | cbz x0,0x00bd4f44 | `CONDITIONAL_JUMP`
<a id="insn-00bd4f20"></a> `00bd4f20` | `82 ee 7c 92` | and x2,x20,#-0x10 | `FALL_THROUGH`
<a id="insn-00bd4f24"></a> `00bd4f24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4f28"></a> `00bd4f28` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bd4f2c"></a> `00bd4f2c` | `85 18 00 94` | bl 0x00bdb140 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4f30"></a> `00bd4f30` | `60 02 02 91` | add x0,x19,#0x80 | `FALL_THROUGH`
<a id="insn-00bd4f34"></a> `00bd4f34` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4f38"></a> `00bd4f38` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd4f3c"></a> `00bd4f3c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd4f40"></a> `00bd4f40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd4f44"></a> `00bd4f44` | `63 18 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd4efc`](#insn-00bd4efc) 範囲 `[['00bd4efc', '00bd4f1f']]`
  - `CONDITIONAL_JUMP` [`00bd4f1c`](#insn-00bd4f1c) → [`00bd4f44`](#insn-00bd4f44)
  - `FALL_THROUGH` [`00bd4f1c`](#insn-00bd4f1c) → [`00bd4f20`](#insn-00bd4f20)
- ブロック [`00bd4f20`](#insn-00bd4f20) 範囲 `[['00bd4f20', '00bd4f2b']]`
  - `FALL_THROUGH` [`00bd4f28`](#insn-00bd4f28) → [`00bd4f2c`](#insn-00bd4f2c)
- ブロック [`00bd4f2c`](#insn-00bd4f2c) 範囲 `[['00bd4f2c', '00bd4f43']]`
- ブロック [`00bd4f44`](#insn-00bd4f44) 範囲 `[['00bd4f44', '00bd4f47']]`

## 命令位置別の参照

- [`00bd4f00`](#insn-00bd4f00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f04`](#insn-00bd4f04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f14`](#insn-00bd4f14) → [`00bd56c8`](../00bd5/00bd56c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd56c8` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f1c`](#insn-00bd4f1c) → [`00bd4f44`](#insn-00bd4f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f2c`](#insn-00bd4f2c) → [`00bdb140`](../00bdb/00bdb140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb140` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f34`](#insn-00bd4f34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f38`](#insn-00bd4f38) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4f44`](#insn-00bd4f44) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd4f00`](#insn-00bd4f00)

~~~json
{
  "source": "00bd4f00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f04`](#insn-00bd4f04)

~~~json
{
  "source": "00bd4f04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f14`](#insn-00bd4f14)

~~~json
{
  "source": "00bd4f14",
  "target": "00bd56c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4f1c`](#insn-00bd4f1c)

~~~json
{
  "source": "00bd4f1c",
  "target": "00bd4f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f2c`](#insn-00bd4f2c)

~~~json
{
  "source": "00bd4f2c",
  "target": "00bdb140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4f34`](#insn-00bd4f34)

~~~json
{
  "source": "00bd4f34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f38`](#insn-00bd4f38)

~~~json
{
  "source": "00bd4f38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4f44`](#insn-00bd4f44)

~~~json
{
  "source": "00bd4f44",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
