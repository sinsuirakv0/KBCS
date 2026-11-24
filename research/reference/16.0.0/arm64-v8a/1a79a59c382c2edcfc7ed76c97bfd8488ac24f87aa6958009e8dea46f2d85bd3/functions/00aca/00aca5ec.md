# 00aca5ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6c658`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c658.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-78dee9fdbcd15a4bda36d3ffc8bc33cb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aca7e8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca7e8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-ce54340c9981b09d2ad8883157dead44)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca5ec",
  "name": "FUN_00aca5ec",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1",
  "source_text_sha256": "1b4ca553e52312c8304e84a7039b242732cd95da5214a33d2ba3a0feefdb30d1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca5ec",
        "00aca643"
      ]
    ],
    "bytes_sha256": "1b41ce593a79ef86c7cc72d0446d9324a84859cdb4abd552a996f74898c2da1f",
    "instruction_count": 22,
    "instruction_bytes": 88,
    "body_bytes": 88,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6d58](../008b6/008b6d58.md)
- [008b7984](../008b7/008b7984.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_00aca5ec(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  
  if ((*(int *)(param_1 + 4) != -1) && (*(char *)(param_1 + 0x14) == '\0')) {
    lVar1 = FUN_008514b8();
    uVar2 = FUN_008b7984(lVar1 + 0x2f38,*(undefined4 *)(param_1 + 4));
    FUN_008b6d58(uVar2,0,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca5ec"></a> `00aca5ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aca5f0"></a> `00aca5f0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca5f4"></a> `00aca5f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aca5f8"></a> `00aca5f8` | `08 04 40 b9` | ldr w8,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00aca5fc"></a> `00aca5fc` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aca600"></a> `00aca600` | `c0 01 00 54` | b.eq 0x00aca638 | `CONDITIONAL_JUMP`
<a id="insn-00aca604"></a> `00aca604` | `08 50 40 39` | ldrb w8,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-00aca608"></a> `00aca608` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca60c"></a> `00aca60c` | `68 01 00 35` | cbnz w8,0x00aca638 | `CONDITIONAL_JUMP`
<a id="insn-00aca610"></a> `00aca610` | `aa 1b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aca614"></a> `00aca614` | `61 06 40 b9` | ldr w1,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aca618"></a> `00aca618` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-00aca61c"></a> `00aca61c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00aca620"></a> `00aca620` | `d9 b4 f7 97` | bl 0x008b7984 | `UNCONDITIONAL_CALL`
<a id="insn-00aca624"></a> `00aca624` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca628"></a> `00aca628` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aca62c"></a> `00aca62c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca630"></a> `00aca630` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aca634"></a> `00aca634` | `c9 b1 f7 17` | b 0x008b6d58 | `CALL_TERMINATOR`
<a id="insn-00aca638"></a> `00aca638` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca63c"></a> `00aca63c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aca640"></a> `00aca640` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca5ec`](#insn-00aca5ec) 範囲 `[['00aca5ec', '00aca603']]`
  - `CONDITIONAL_JUMP` [`00aca600`](#insn-00aca600) → [`00aca638`](#insn-00aca638)
  - `FALL_THROUGH` [`00aca600`](#insn-00aca600) → [`00aca604`](#insn-00aca604)
- ブロック [`00aca604`](#insn-00aca604) 範囲 `[['00aca604', '00aca60f']]`
  - `CONDITIONAL_JUMP` [`00aca60c`](#insn-00aca60c) → [`00aca638`](#insn-00aca638)
  - `FALL_THROUGH` [`00aca60c`](#insn-00aca60c) → [`00aca610`](#insn-00aca610)
- ブロック [`00aca610`](#insn-00aca610) 範囲 `[['00aca610', '00aca637']]`
- ブロック [`00aca638`](#insn-00aca638) 範囲 `[['00aca638', '00aca643']]`

## 命令位置別の参照

- [`00aca5ec`](#insn-00aca5ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca5f0`](#insn-00aca5f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca600`](#insn-00aca600) → [`00aca638`](#insn-00aca638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca60c`](#insn-00aca60c) → [`00aca638`](#insn-00aca638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca610`](#insn-00aca610) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aca620`](#insn-00aca620) → [`008b7984`](../008b7/008b7984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7984` · 推定シンボル `None` · 推定型 `None`
- [`00aca62c`](#insn-00aca62c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca630`](#insn-00aca630) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca634`](#insn-00aca634) → [`008b6d58`](../008b6/008b6d58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6d58` · 推定シンボル `None` · 推定型 `None`
- [`00aca638`](#insn-00aca638) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca63c`](#insn-00aca63c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca5ec`](#insn-00aca5ec)

~~~json
{
  "source": "00aca5ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca5f0`](#insn-00aca5f0)

~~~json
{
  "source": "00aca5f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca600`](#insn-00aca600)

~~~json
{
  "source": "00aca600",
  "target": "00aca638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca60c`](#insn-00aca60c)

~~~json
{
  "source": "00aca60c",
  "target": "00aca638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca610`](#insn-00aca610)

~~~json
{
  "source": "00aca610",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca620`](#insn-00aca620)

~~~json
{
  "source": "00aca620",
  "target": "008b7984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca62c`](#insn-00aca62c)

~~~json
{
  "source": "00aca62c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca630`](#insn-00aca630)

~~~json
{
  "source": "00aca630",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca634`](#insn-00aca634)

~~~json
{
  "source": "00aca634",
  "target": "008b6d58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca638`](#insn-00aca638)

~~~json
{
  "source": "00aca638",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca63c`](#insn-00aca63c)

~~~json
{
  "source": "00aca63c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
