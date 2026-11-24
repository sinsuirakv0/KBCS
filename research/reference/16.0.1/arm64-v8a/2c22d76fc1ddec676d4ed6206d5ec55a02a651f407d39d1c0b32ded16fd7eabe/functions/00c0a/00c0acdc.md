# 00c0acdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0a8b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-a762632cce91dee999dd08bd4a58dc8b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c0ad78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0ad78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-cc2775c739acd7939118a7cdded39230)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0acdc",
  "name": "_ZNSt6__ndk16__clocEv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "371bc99a0cbee51e8c73f468ef7d91c7add292481e190391bfa3018dd1caca01",
  "source_text_sha256": "371bc99a0cbee51e8c73f468ef7d91c7add292481e190391bfa3018dd1caca01",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0acdc",
        "00c0ad4b"
      ]
    ],
    "bytes_sha256": "252439929b224c608be1bfea7a35873c1ea99f273a4233db0bd45357f908f8e7",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c5d220](../00c5d/00c5d220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 282 bytes

~~~c

__locale_t _ZNSt6__ndk16__clocEv(void)

{
  int iVar1;
  
  if (((DAT_01127ca0 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01127ca0), iVar1 != 0)) {
    DAT_01127c98 = newlocale(0x1fbf,"C",(__locale_t)0x0);
    __cxa_guard_release(&DAT_01127ca0);
  }
  return DAT_01127c98;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0acdc"></a> `00c0acdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0ace0"></a> `00c0ace0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00c0ace4"></a> `00c0ace4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0ace8"></a> `00c0ace8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c0acec"></a> `00c0acec` | `e8 28 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0acf0"></a> `00c0acf0` | `08 81 32 91` | add x8,x8,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0acf4"></a> `00c0acf4` | `f3 28 00 b0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0acf8"></a> `00c0acf8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c0acfc"></a> `00c0acfc` | `c8 00 00 36` | tbz w8,#0x0,0x00c0ad14 | `CONDITIONAL_JUMP`
<a id="insn-00c0ad00"></a> `00c0ad00` | `60 4e 46 f9` | ldr x0,[x19, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0ad04"></a> `00c0ad04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c0ad08"></a> `00c0ad08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00c0ad0c"></a> `00c0ad0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0ad10"></a> `00c0ad10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c0ad14"></a> `00c0ad14` | `e0 28 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0ad18"></a> `00c0ad18` | `00 80 32 91` | add x0,x0,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0ad1c"></a> `00c0ad1c` | `4d 34 01 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ad20"></a> `00c0ad20` | `00 ff ff 34` | cbz w0,0x00c0ad00 | `CONDITIONAL_JUMP`
<a id="insn-00c0ad24"></a> `00c0ad24` | `61 b5 ff 90` | adrp x1,0x2b6000 | `FALL_THROUGH`
<a id="insn-00c0ad28"></a> `00c0ad28` | `21 f0 05 91` | add x1,x1,#0x17c | `FALL_THROUGH`
<a id="insn-00c0ad2c"></a> `00c0ad2c` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00c0ad30"></a> `00c0ad30` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00c0ad34"></a> `00c0ad34` | `3b 49 01 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ad38"></a> `00c0ad38` | `60 4e 06 f9` | str x0,[x19, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0ad3c"></a> `00c0ad3c` | `e0 28 00 b0` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0ad40"></a> `00c0ad40` | `00 80 32 91` | add x0,x0,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0ad44"></a> `00c0ad44` | `4b 34 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0ad48"></a> `00c0ad48` | `ee ff ff 17` | b 0x00c0ad00 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c0acdc`](#insn-00c0acdc) 範囲 `[['00c0acdc', '00c0acff']]`
  - `CONDITIONAL_JUMP` [`00c0acfc`](#insn-00c0acfc) → [`00c0ad14`](#insn-00c0ad14)
  - `FALL_THROUGH` [`00c0acfc`](#insn-00c0acfc) → [`00c0ad00`](#insn-00c0ad00)
- ブロック [`00c0ad00`](#insn-00c0ad00) 範囲 `[['00c0ad00', '00c0ad13']]`
- ブロック [`00c0ad14`](#insn-00c0ad14) 範囲 `[['00c0ad14', '00c0ad23']]`
  - `CONDITIONAL_JUMP` [`00c0ad20`](#insn-00c0ad20) → [`00c0ad00`](#insn-00c0ad00)
  - `FALL_THROUGH` [`00c0ad20`](#insn-00c0ad20) → [`00c0ad24`](#insn-00c0ad24)
- ブロック [`00c0ad24`](#insn-00c0ad24) 範囲 `[['00c0ad24', '00c0ad4b']]`
  - `UNCONDITIONAL_JUMP` [`00c0ad48`](#insn-00c0ad48) → [`00c0ad00`](#insn-00c0ad00)

## 命令位置別の参照

- [`00c0ace0`](#insn-00c0ace0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ace4`](#insn-00c0ace4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0acf8`](#insn-00c0acf8) → `01127ca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0acfc`](#insn-00c0acfc) → [`00c0ad14`](#insn-00c0ad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad00`](#insn-00c0ad00) → `01127c98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c0ad04`](#insn-00c0ad04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad08`](#insn-00c0ad08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad18`](#insn-00c0ad18) → `01127ca0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0ad1c`](#insn-00c0ad1c) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad20`](#insn-00c0ad20) → [`00c0ad00`](#insn-00c0ad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad28`](#insn-00c0ad28) → `002b617c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad34`](#insn-00c0ad34) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad38`](#insn-00c0ad38) → `01127c98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c0ad40`](#insn-00c0ad40) → `01127ca0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0ad44`](#insn-00c0ad44) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c0ad48`](#insn-00c0ad48) → [`00c0ad00`](#insn-00c0ad00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0ace0`](#insn-00c0ace0)

~~~json
{
  "source": "00c0ace0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ace4`](#insn-00c0ace4)

~~~json
{
  "source": "00c0ace4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0acf8`](#insn-00c0acf8)

~~~json
{
  "source": "00c0acf8",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0acfc`](#insn-00c0acfc)

~~~json
{
  "source": "00c0acfc",
  "target": "00c0ad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ad00`](#insn-00c0ad00)

~~~json
{
  "source": "00c0ad00",
  "target": "01127c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ad04`](#insn-00c0ad04)

~~~json
{
  "source": "00c0ad04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ad08`](#insn-00c0ad08)

~~~json
{
  "source": "00c0ad08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ad18`](#insn-00c0ad18)

~~~json
{
  "source": "00c0ad18",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ad1c`](#insn-00c0ad1c)

~~~json
{
  "source": "00c0ad1c",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ad20`](#insn-00c0ad20)

~~~json
{
  "source": "00c0ad20",
  "target": "00c0ad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ad28`](#insn-00c0ad28)

~~~json
{
  "source": "00c0ad28",
  "target": "002b617c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0ad34`](#insn-00c0ad34)

~~~json
{
  "source": "00c0ad34",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ad38`](#insn-00c0ad38)

~~~json
{
  "source": "00c0ad38",
  "target": "01127c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ad40`](#insn-00c0ad40)

~~~json
{
  "source": "00c0ad40",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0ad44`](#insn-00c0ad44)

~~~json
{
  "source": "00c0ad44",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0ad48`](#insn-00c0ad48)

~~~json
{
  "source": "00c0ad48",
  "target": "00c0ad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
