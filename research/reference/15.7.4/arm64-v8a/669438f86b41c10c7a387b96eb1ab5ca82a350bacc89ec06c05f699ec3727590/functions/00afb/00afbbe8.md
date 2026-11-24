# 00afbbe8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afbba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbba4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-be19faf2c45f0efaa56d5d84959d4da0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5b96c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b96c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-166254ae2ea44d273c938d45c13f56a2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbbe8",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6",
  "source_text_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbbe8",
        "00afbc6f"
      ]
    ],
    "bytes_sha256": "8b7c9b392646fd72c17703e313adf3838717769357ea2b30fc87908498edfb84",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7d0](../00bdb/00bdb7d0.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec90](../00bde/00bdec90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0d38 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbc10 to 00bfbc17 has its CatchHandler @ 00aff45c */
    if ((__thread1 == 0) || (DAT_010a0d40 == 0)) {
      if (DAT_010a0d40 != 0 || __thread1 != 0) goto LAB_00afbc60;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0d40);
      if (iVar1 == 0) goto LAB_00afbc60;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbc40 to 00bfbc57 has its CatchHandler @ 00aff458 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbc60:
                    /* try { // try from 00afbc68 to 00bfbc7f has its CatchHandler @ 00b003c0 */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbbe8"></a> `00afbbe8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afbbec"></a> `00afbbec` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbbf0"></a> `00afbbf0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afbbf4"></a> `00afbbf4` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbbf8"></a> `00afbbf8` | `08 e1 74 39` | ldrb w8,[x8, #0xd38] | `FALL_THROUGH`
<a id="insn-00afbbfc"></a> `00afbbfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbc00"></a> `00afbc00` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbc04"></a> `00afbc04` | `e1 02 00 54` | b.ne 0x00afbc60 | `CONDITIONAL_JUMP`
<a id="insn-00afbc08"></a> `00afbc08` | `f2 7e 03 94` | bl 0x00bdb7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbc0c"></a> `00afbc0c` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbc10"></a> `00afbc10` | `01 a1 46 f9` | ldr x1,[x8, #0xd40] | `FALL_THROUGH`
<a id="insn-00afbc14"></a> `00afbc14` | `20 02 00 b4` | cbz x0,0x00afbc58 | `CONDITIONAL_JUMP`
<a id="insn-00afbc18"></a> `00afbc18` | `01 02 00 b4` | cbz x1,0x00afbc58 | `CONDITIONAL_JUMP`
<a id="insn-00afbc1c"></a> `00afbc1c` | `1d 8c 03 94` | bl 0x00bdec90 | `UNCONDITIONAL_CALL`
<a id="insn-00afbc20"></a> `00afbc20` | `00 02 00 34` | cbz w0,0x00afbc60 | `CONDITIONAL_JUMP`
<a id="insn-00afbc24"></a> `00afbc24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbc28"></a> `00afbc28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc2c"></a> `00afbc2c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc30"></a> `00afbc30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbc34"></a> `00afbc34` | `b3 00 00 b4` | cbz x19,0x00afbc48 | `CONDITIONAL_JUMP`
<a id="insn-00afbc38"></a> `00afbc38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbc3c"></a> `00afbc3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc40"></a> `00afbc40` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbc44"></a> `00afbc44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbc48"></a> `00afbc48` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc4c"></a> `00afbc4c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00afbc50"></a> `00afbc50` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbc54"></a> `00afbc54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afbc58"></a> `00afbc58` | `28 00 00 aa` | orr x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00afbc5c"></a> `00afbc5c` | `48 fe ff b4` | cbz x8,0x00afbc24 | `CONDITIONAL_JUMP`
<a id="insn-00afbc60"></a> `00afbc60` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc64"></a> `00afbc64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc68"></a> `00afbc68` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbc6c"></a> `00afbc6c` | `f1 8b 03 14` | b 0x00bdec30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbbe8`](#insn-00afbbe8) 範囲 `[['00afbbe8', '00afbc07']]`
  - `CONDITIONAL_JUMP` [`00afbc04`](#insn-00afbc04) → [`00afbc60`](#insn-00afbc60)
  - `FALL_THROUGH` [`00afbc04`](#insn-00afbc04) → [`00afbc08`](#insn-00afbc08)
- ブロック [`00afbc08`](#insn-00afbc08) 範囲 `[['00afbc08', '00afbc0f']]`
  - `FALL_THROUGH` [`00afbc0c`](#insn-00afbc0c) → [`00afbc10`](#insn-00afbc10)
- ブロック [`00afbc10`](#insn-00afbc10) 範囲 `[['00afbc10', '00afbc17']]`
  - `CONDITIONAL_JUMP` [`00afbc14`](#insn-00afbc14) → [`00afbc58`](#insn-00afbc58)
  - `FALL_THROUGH` [`00afbc14`](#insn-00afbc14) → [`00afbc18`](#insn-00afbc18)
- ブロック [`00afbc18`](#insn-00afbc18) 範囲 `[['00afbc18', '00afbc1b']]`
  - `CONDITIONAL_JUMP` [`00afbc18`](#insn-00afbc18) → [`00afbc58`](#insn-00afbc58)
  - `FALL_THROUGH` [`00afbc18`](#insn-00afbc18) → [`00afbc1c`](#insn-00afbc1c)
- ブロック [`00afbc1c`](#insn-00afbc1c) 範囲 `[['00afbc1c', '00afbc23']]`
  - `CONDITIONAL_JUMP` [`00afbc20`](#insn-00afbc20) → [`00afbc60`](#insn-00afbc60)
  - `FALL_THROUGH` [`00afbc20`](#insn-00afbc20) → [`00afbc24`](#insn-00afbc24)
- ブロック [`00afbc24`](#insn-00afbc24) 範囲 `[['00afbc24', '00afbc37']]`
  - `CONDITIONAL_JUMP` [`00afbc34`](#insn-00afbc34) → [`00afbc48`](#insn-00afbc48)
  - `FALL_THROUGH` [`00afbc34`](#insn-00afbc34) → [`00afbc38`](#insn-00afbc38)
- ブロック [`00afbc38`](#insn-00afbc38) 範囲 `[['00afbc38', '00afbc3f']]`
  - `FALL_THROUGH` [`00afbc3c`](#insn-00afbc3c) → [`00afbc40`](#insn-00afbc40)
- ブロック [`00afbc40`](#insn-00afbc40) 範囲 `[['00afbc40', '00afbc47']]`
  - `FALL_THROUGH` [`00afbc44`](#insn-00afbc44) → [`00afbc48`](#insn-00afbc48)
- ブロック [`00afbc48`](#insn-00afbc48) 範囲 `[['00afbc48', '00afbc57']]`
- ブロック [`00afbc58`](#insn-00afbc58) 範囲 `[['00afbc58', '00afbc5f']]`
  - `CONDITIONAL_JUMP` [`00afbc5c`](#insn-00afbc5c) → [`00afbc24`](#insn-00afbc24)
  - `FALL_THROUGH` [`00afbc5c`](#insn-00afbc5c) → [`00afbc60`](#insn-00afbc60)
- ブロック [`00afbc60`](#insn-00afbc60) 範囲 `[['00afbc60', '00afbc67']]`
  - `FALL_THROUGH` [`00afbc64`](#insn-00afbc64) → [`00afbc68`](#insn-00afbc68)
- ブロック [`00afbc68`](#insn-00afbc68) 範囲 `[['00afbc68', '00afbc6f']]`

## 命令位置別の参照

- [`00afbbe8`](#insn-00afbbe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbec`](#insn-00afbbec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbf8`](#insn-00afbbf8) → `010a0d38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00afbc04`](#insn-00afbc04) → [`00afbc60`](#insn-00afbc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc08`](#insn-00afbc08) → [`00bdb7d0`](../00bdb/00bdb7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7d0` · 推定シンボル `None` · 推定型 `None`
- [`00afbc10`](#insn-00afbc10) → `010a0d40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbc14`](#insn-00afbc14) → [`00afbc58`](#insn-00afbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc18`](#insn-00afbc18) → [`00afbc58`](#insn-00afbc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc1c`](#insn-00afbc1c) → [`00bdec90`](../00bde/00bdec90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec90` · 推定シンボル `None` · 推定型 `None`
- [`00afbc20`](#insn-00afbc20) → [`00afbc60`](#insn-00afbc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc34`](#insn-00afbc34) → [`00afbc48`](#insn-00afbc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc48`](#insn-00afbc48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc5c`](#insn-00afbc5c) → [`00afbc24`](#insn-00afbc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc60`](#insn-00afbc60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc6c`](#insn-00afbc6c) → [`00bdec30`](../00bde/00bdec30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbbe8`](#insn-00afbbe8)

~~~json
{
  "source": "00afbbe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbec`](#insn-00afbbec)

~~~json
{
  "source": "00afbbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbf8`](#insn-00afbbf8)

~~~json
{
  "source": "00afbbf8",
  "target": "010a0d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbc04`](#insn-00afbc04)

~~~json
{
  "source": "00afbc04",
  "target": "00afbc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc08`](#insn-00afbc08)

~~~json
{
  "source": "00afbc08",
  "target": "00bdb7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbc10`](#insn-00afbc10)

~~~json
{
  "source": "00afbc10",
  "target": "010a0d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbc14`](#insn-00afbc14)

~~~json
{
  "source": "00afbc14",
  "target": "00afbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc18`](#insn-00afbc18)

~~~json
{
  "source": "00afbc18",
  "target": "00afbc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc1c`](#insn-00afbc1c)

~~~json
{
  "source": "00afbc1c",
  "target": "00bdec90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbc20`](#insn-00afbc20)

~~~json
{
  "source": "00afbc20",
  "target": "00afbc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc34`](#insn-00afbc34)

~~~json
{
  "source": "00afbc34",
  "target": "00afbc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc48`](#insn-00afbc48)

~~~json
{
  "source": "00afbc48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc5c`](#insn-00afbc5c)

~~~json
{
  "source": "00afbc5c",
  "target": "00afbc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc60`](#insn-00afbc60)

~~~json
{
  "source": "00afbc60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc6c`](#insn-00afbc6c)

~~~json
{
  "source": "00afbc6c",
  "target": "00bdec30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
