# 00bfaff0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfabc8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfabc8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-0e2ed90b512dbc4f1295225d3078ceb9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfb08c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfb08c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-ece620a77bb6261c61a6350e09c557ff)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaff0",
  "name": "_ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c",
  "source_text_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaff0",
        "00bfb053"
      ]
    ],
    "bytes_sha256": "39015776d512796c9c9fe178f10a4e3c36ad30be01d1672470206a10148c8dcf",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5e2d0](../00c5e/00c5e2d0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 423 bytes

~~~c

void _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(long param_1,undefined4 param_2)

{
  long lVar1;
  
  if (*(long *)(param_1 + 0x48) != 0) {
    lVar1 = *(long *)(param_1 + 0x48) + -1;
    do {
      (**(code **)(*(long *)(param_1 + 0x38) + lVar1 * 8))
                (param_2,param_1,*(undefined4 *)(*(long *)(param_1 + 0x40) + lVar1 * 4));
      lVar1 = lVar1 + -1;
    } while (lVar1 != -1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaff0"></a> `00bfaff0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfaff4"></a> `00bfaff4` | `08 24 40 f9` | ldr x8,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bfaff8"></a> `00bfaff8` | `c8 02 00 b4` | cbz x8,0x00bfb050 | `CONDITIONAL_JUMP`
<a id="insn-00bfaffc"></a> `00bfaffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb000"></a> `00bfb000` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfb004"></a> `00bfb004` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb008"></a> `00bfb008` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb00c"></a> `00bfb00c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb010"></a> `00bfb010` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb014"></a> `00bfb014` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bfb018"></a> `00bfb018` | `15 05 00 d1` | sub x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb01c"></a> `00bfb01c` | `68 a6 43 a9` | ldp x8,x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb020"></a> `00bfb020` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bfb024"></a> `00bfb024` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfb028"></a> `00bfb028` | `08 79 75 f8` | ldr x8,[x8, x21, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfb02c"></a> `00bfb02c` | `22 79 75 b8` | ldr w2,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bfb030"></a> `00bfb030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfb034"></a> `00bfb034` | `b5 06 00 d1` | sub x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb038"></a> `00bfb038` | `bf 06 00 b1` | cmn x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb03c"></a> `00bfb03c` | `01 ff ff 54` | b.ne 0x00bfb01c | `CONDITIONAL_JUMP`
<a id="insn-00bfb040"></a> `00bfb040` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb044"></a> `00bfb044` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb048"></a> `00bfb048` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfb04c"></a> `00bfb04c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb050"></a> `00bfb050` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaff0`](#insn-00bfaff0) 範囲 `[['00bfaff0', '00bfaffb']]`
  - `CONDITIONAL_JUMP` [`00bfaff8`](#insn-00bfaff8) → [`00bfb050`](#insn-00bfb050)
  - `FALL_THROUGH` [`00bfaff8`](#insn-00bfaff8) → [`00bfaffc`](#insn-00bfaffc)
- ブロック [`00bfaffc`](#insn-00bfaffc) 範囲 `[['00bfaffc', '00bfb01b']]`
  - `FALL_THROUGH` [`00bfb018`](#insn-00bfb018) → [`00bfb01c`](#insn-00bfb01c)
- ブロック [`00bfb01c`](#insn-00bfb01c) 範囲 `[['00bfb01c', '00bfb03f']]`
  - `CONDITIONAL_JUMP` [`00bfb03c`](#insn-00bfb03c) → [`00bfb01c`](#insn-00bfb01c)
  - `FALL_THROUGH` [`00bfb03c`](#insn-00bfb03c) → [`00bfb040`](#insn-00bfb040)
- ブロック [`00bfb040`](#insn-00bfb040) 範囲 `[['00bfb040', '00bfb04f']]`
  - `FALL_THROUGH` [`00bfb04c`](#insn-00bfb04c) → [`00bfb050`](#insn-00bfb050)
- ブロック [`00bfb050`](#insn-00bfb050) 範囲 `[['00bfb050', '00bfb053']]`

## 命令位置別の参照

- [`00bfaff8`](#insn-00bfaff8) → [`00bfb050`](#insn-00bfb050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb000`](#insn-00bfb000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb004`](#insn-00bfb004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb008`](#insn-00bfb008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb03c`](#insn-00bfb03c) → [`00bfb01c`](#insn-00bfb01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb040`](#insn-00bfb040) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb044`](#insn-00bfb044) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb048`](#insn-00bfb048) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaff8`](#insn-00bfaff8)

~~~json
{
  "source": "00bfaff8",
  "target": "00bfb050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb000`](#insn-00bfb000)

~~~json
{
  "source": "00bfb000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb004`](#insn-00bfb004)

~~~json
{
  "source": "00bfb004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb008`](#insn-00bfb008)

~~~json
{
  "source": "00bfb008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb03c`](#insn-00bfb03c)

~~~json
{
  "source": "00bfb03c",
  "target": "00bfb01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb040`](#insn-00bfb040)

~~~json
{
  "source": "00bfb040",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb044`](#insn-00bfb044)

~~~json
{
  "source": "00bfb044",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb048`](#insn-00bfb048)

~~~json
{
  "source": "00bfb048",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
