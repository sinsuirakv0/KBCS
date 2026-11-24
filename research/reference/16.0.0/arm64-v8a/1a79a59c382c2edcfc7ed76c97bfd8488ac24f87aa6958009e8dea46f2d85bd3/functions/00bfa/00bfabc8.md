# 00bfabc8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e180`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e180.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-1150b1fa3f51fae46f93c3ffc82a8438)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfaff0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaff0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-0e2ed90b512dbc4f1295225d3078ceb9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfabc8",
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
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfabc8",
        "00bfac2b"
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

- [00c5ded0](../00c5d/00c5ded0.md)

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
<a id="insn-00bfabc8"></a> `00bfabc8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfabcc"></a> `00bfabcc` | `08 24 40 f9` | ldr x8,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bfabd0"></a> `00bfabd0` | `c8 02 00 b4` | cbz x8,0x00bfac28 | `CONDITIONAL_JUMP`
<a id="insn-00bfabd4"></a> `00bfabd4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfabd8"></a> `00bfabd8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfabdc"></a> `00bfabdc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfabe0"></a> `00bfabe0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfabe4"></a> `00bfabe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfabe8"></a> `00bfabe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfabec"></a> `00bfabec` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bfabf0"></a> `00bfabf0` | `15 05 00 d1` | sub x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfabf4"></a> `00bfabf4` | `68 a6 43 a9` | ldp x8,x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bfabf8"></a> `00bfabf8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bfabfc"></a> `00bfabfc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfac00"></a> `00bfac00` | `08 79 75 f8` | ldr x8,[x8, x21, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfac04"></a> `00bfac04` | `22 79 75 b8` | ldr w2,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bfac08"></a> `00bfac08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfac0c"></a> `00bfac0c` | `b5 06 00 d1` | sub x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac10"></a> `00bfac10` | `bf 06 00 b1` | cmn x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfac14"></a> `00bfac14` | `01 ff ff 54` | b.ne 0x00bfabf4 | `CONDITIONAL_JUMP`
<a id="insn-00bfac18"></a> `00bfac18` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfac1c"></a> `00bfac1c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac20"></a> `00bfac20` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfac24"></a> `00bfac24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfac28"></a> `00bfac28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfabc8`](#insn-00bfabc8) 範囲 `[['00bfabc8', '00bfabd3']]`
  - `CONDITIONAL_JUMP` [`00bfabd0`](#insn-00bfabd0) → [`00bfac28`](#insn-00bfac28)
  - `FALL_THROUGH` [`00bfabd0`](#insn-00bfabd0) → [`00bfabd4`](#insn-00bfabd4)
- ブロック [`00bfabd4`](#insn-00bfabd4) 範囲 `[['00bfabd4', '00bfabf3']]`
  - `FALL_THROUGH` [`00bfabf0`](#insn-00bfabf0) → [`00bfabf4`](#insn-00bfabf4)
- ブロック [`00bfabf4`](#insn-00bfabf4) 範囲 `[['00bfabf4', '00bfac17']]`
  - `CONDITIONAL_JUMP` [`00bfac14`](#insn-00bfac14) → [`00bfabf4`](#insn-00bfabf4)
  - `FALL_THROUGH` [`00bfac14`](#insn-00bfac14) → [`00bfac18`](#insn-00bfac18)
- ブロック [`00bfac18`](#insn-00bfac18) 範囲 `[['00bfac18', '00bfac27']]`
  - `FALL_THROUGH` [`00bfac24`](#insn-00bfac24) → [`00bfac28`](#insn-00bfac28)
- ブロック [`00bfac28`](#insn-00bfac28) 範囲 `[['00bfac28', '00bfac2b']]`

## 命令位置別の参照

- [`00bfabd0`](#insn-00bfabd0) → [`00bfac28`](#insn-00bfac28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabd8`](#insn-00bfabd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabdc`](#insn-00bfabdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabe0`](#insn-00bfabe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac14`](#insn-00bfac14) → [`00bfabf4`](#insn-00bfabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac18`](#insn-00bfac18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac1c`](#insn-00bfac1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac20`](#insn-00bfac20) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfabd0`](#insn-00bfabd0)

~~~json
{
  "source": "00bfabd0",
  "target": "00bfac28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabd8`](#insn-00bfabd8)

~~~json
{
  "source": "00bfabd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabdc`](#insn-00bfabdc)

~~~json
{
  "source": "00bfabdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabe0`](#insn-00bfabe0)

~~~json
{
  "source": "00bfabe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac14`](#insn-00bfac14)

~~~json
{
  "source": "00bfac14",
  "target": "00bfabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac18`](#insn-00bfac18)

~~~json
{
  "source": "00bfac18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac1c`](#insn-00bfac1c)

~~~json
{
  "source": "00bfac1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac20`](#insn-00bfac20)

~~~json
{
  "source": "00bfac20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
