# 00baaff8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baaf30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf30.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-130882ff06ae6505da536080a7d30274)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bab03c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab03c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-56e4006805b19e884cead5758015945f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaff8",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9460ee0e26ff0bf6dfad04cfe5cef8e6b5ae00bd8b017952c92dae49be721d2a",
  "source_text_sha256": "9460ee0e26ff0bf6dfad04cfe5cef8e6b5ae00bd8b017952c92dae49be721d2a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaff8",
        "00bab053"
      ]
    ],
    "bytes_sha256": "7ca844b809d9a31e60a90ffb2048d6214d9d41a335809353cbbdaedcb3a4bc86",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1aa0](../00be1/00be1aa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 373 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEPwPKw
                   (long param_1,wint_t *param_2,wint_t *param_3)

{
  wint_t *pwVar1;
  wint_t wVar2;
  
  pwVar1 = param_2;
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    wVar2 = towlower_l(*param_2,*(__locale_t *)(param_1 + 0x10));
    *param_2 = wVar2;
    pwVar1 = param_3;
  }
  return pwVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaff8"></a> `00baaff8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baaffc"></a> `00baaffc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bab00c"></a> `00bab00c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `40 01 00 54` | b.eq 0x00bab03c | `CONDITIONAL_JUMP`
<a id="insn-00bab018"></a> `00bab018` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bab028"></a> `00bab028` | `9e da 00 94` | bl 0x00be1aa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab02c"></a> `00bab02c` | `60 46 00 b8` | str w0,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00bab030"></a> `00bab030` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bab034"></a> `00bab034` | `61 ff ff 54` | b.ne 0x00bab020 | `CONDITIONAL_JUMP`
<a id="insn-00bab038"></a> `00bab038` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00bab03c"></a> `00bab03c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bab040"></a> `00bab040` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab044"></a> `00bab044` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab048"></a> `00bab048` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bab04c"></a> `00bab04c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bab050"></a> `00bab050` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaff8`](#insn-00baaff8) 範囲 `[['00baaff8', '00bab017']]`
  - `CONDITIONAL_JUMP` [`00bab014`](#insn-00bab014) → [`00bab03c`](#insn-00bab03c)
  - `FALL_THROUGH` [`00bab014`](#insn-00bab014) → [`00bab018`](#insn-00bab018)
- ブロック [`00bab018`](#insn-00bab018) 範囲 `[['00bab018', '00bab01f']]`
  - `FALL_THROUGH` [`00bab01c`](#insn-00bab01c) → [`00bab020`](#insn-00bab020)
- ブロック [`00bab020`](#insn-00bab020) 範囲 `[['00bab020', '00bab037']]`
  - `CONDITIONAL_JUMP` [`00bab034`](#insn-00bab034) → [`00bab020`](#insn-00bab020)
  - `FALL_THROUGH` [`00bab034`](#insn-00bab034) → [`00bab038`](#insn-00bab038)
- ブロック [`00bab038`](#insn-00bab038) 範囲 `[['00bab038', '00bab03b']]`
  - `FALL_THROUGH` [`00bab038`](#insn-00bab038) → [`00bab03c`](#insn-00bab03c)
- ブロック [`00bab03c`](#insn-00bab03c) 範囲 `[['00bab03c', '00bab053']]`

## 命令位置別の参照

- [`00baaffc`](#insn-00baaffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab000`](#insn-00bab000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab004`](#insn-00bab004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab014`](#insn-00bab014) → [`00bab03c`](#insn-00bab03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab028`](#insn-00bab028) → [`00be1aa0`](../00be1/00be1aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1aa0` · 推定シンボル `None` · 推定型 `None`
- [`00bab034`](#insn-00bab034) → [`00bab020`](#insn-00bab020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab040`](#insn-00bab040) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab044`](#insn-00bab044) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab048`](#insn-00bab048) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaffc`](#insn-00baaffc)

~~~json
{
  "source": "00baaffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab000`](#insn-00bab000)

~~~json
{
  "source": "00bab000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab004`](#insn-00bab004)

~~~json
{
  "source": "00bab004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab014`](#insn-00bab014)

~~~json
{
  "source": "00bab014",
  "target": "00bab03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab028`](#insn-00bab028)

~~~json
{
  "source": "00bab028",
  "target": "00be1aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab034`](#insn-00bab034)

~~~json
{
  "source": "00bab034",
  "target": "00bab020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab040`](#insn-00bab040)

~~~json
{
  "source": "00bab040",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab044`](#insn-00bab044)

~~~json
{
  "source": "00bab044",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab048`](#insn-00bab048)

~~~json
{
  "source": "00bab048",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
