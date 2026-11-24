# 00adaed8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adae94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00adae94.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-03736f0530c6a2ee6b80624069cc2742)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3a8b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a8b0.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-7e5e21af645ac4aa3900f74f21539a89)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adaed8",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementContentReady",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25df58574dc4b14fcafb76d67a1f82104a686e5dca7b42703e1e20033b694fab",
  "source_text_sha256": "25df58574dc4b14fcafb76d67a1f82104a686e5dca7b42703e1e20033b694fab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adaed8",
        "00adaf67"
      ],
      [
        "00adaf94",
        "00adaf97"
      ]
    ],
    "bytes_sha256": "3abfede2160deaf2789e411acac7adf6cb6d74ecc0925ecc7a27da7f85e8c30c",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00566a7c](../00566/00566a7c.md)
- [00adba20](../00adb/00adba20.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 793 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementContentReady
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_00566a7c(local_40,param_1,param_3);
  puVar2 = (undefined8 *)FUN_00adba20(&DAT_0109ff38,local_40);
  if ((puVar2 != &DAT_0109ff40) && (plVar3 = (long *)puVar2[0x18], plVar3 != (long *)0x0)) {
    (**(code **)(*plVar3 + 0x30))(plVar3,local_40);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adaed8"></a> `00adaed8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adaedc"></a> `00adaedc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adaee0"></a> `00adaee0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adaee4"></a> `00adaee4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adaee8"></a> `00adaee8` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adaeec"></a> `00adaeec` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00adaef0"></a> `00adaef0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adaef4"></a> `00adaef4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaef8"></a> `00adaef8` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00adaefc"></a> `00adaefc` | `e0 2e ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00adaf00"></a> `00adaf00` | `20 2e 00 b0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaf04"></a> `00adaf04` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00adaf08"></a> `00adaf08` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adaf0c"></a> `00adaf0c` | `c5 02 00 94` | bl 0x00adba20 | `UNCONDITIONAL_CALL`
<a id="insn-00adaf10"></a> `00adaf10` | `28 2e 00 b0` | adrp x8,0x109f000 | `FALL_THROUGH`
<a id="insn-00adaf14"></a> `00adaf14` | `08 01 3d 91` | add x8,x8,#0xf40 | `FALL_THROUGH`
<a id="insn-00adaf18"></a> `00adaf18` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00adaf1c"></a> `00adaf1c` | `e0 00 00 54` | b.eq 0x00adaf38 | `CONDITIONAL_JUMP`
<a id="insn-00adaf20"></a> `00adaf20` | `00 60 40 f9` | ldr x0,[x0, #0xc0] | `FALL_THROUGH`
<a id="insn-00adaf24"></a> `00adaf24` | `a0 00 00 b4` | cbz x0,0x00adaf38 | `CONDITIONAL_JUMP`
<a id="insn-00adaf28"></a> `00adaf28` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00adaf2c"></a> `00adaf2c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00adaf30"></a> `00adaf30` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00adaf34"></a> `00adaf34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adaf38"></a> `00adaf38` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00adaf3c"></a> `00adaf3c` | `68 00 00 36` | tbz w8,#0x0,0x00adaf48 | `CONDITIONAL_JUMP`
<a id="insn-00adaf40"></a> `00adaf40` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adaf44"></a> `00adaf44` | `47 00 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adaf48"></a> `00adaf48` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adaf4c"></a> `00adaf4c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adaf50"></a> `00adaf50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adaf54"></a> `00adaf54` | `01 02 00 54` | b.ne 0x00adaf94 | `CONDITIONAL_JUMP`
<a id="insn-00adaf58"></a> `00adaf58` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adaf5c"></a> `00adaf5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adaf60"></a> `00adaf60` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00adaf64"></a> `00adaf64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adaf94"></a> `00adaf94` | `3f 00 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adaed8`](#insn-00adaed8) 範囲 `[['00adaed8', '00adaf1f']]`
  - `CONDITIONAL_JUMP` [`00adaf1c`](#insn-00adaf1c) → [`00adaf38`](#insn-00adaf38)
  - `FALL_THROUGH` [`00adaf1c`](#insn-00adaf1c) → [`00adaf20`](#insn-00adaf20)
- ブロック [`00adaf20`](#insn-00adaf20) 範囲 `[['00adaf20', '00adaf27']]`
  - `CONDITIONAL_JUMP` [`00adaf24`](#insn-00adaf24) → [`00adaf38`](#insn-00adaf38)
  - `FALL_THROUGH` [`00adaf24`](#insn-00adaf24) → [`00adaf28`](#insn-00adaf28)
- ブロック [`00adaf28`](#insn-00adaf28) 範囲 `[['00adaf28', '00adaf37']]`
  - `FALL_THROUGH` [`00adaf34`](#insn-00adaf34) → [`00adaf38`](#insn-00adaf38)
- ブロック [`00adaf38`](#insn-00adaf38) 範囲 `[['00adaf38', '00adaf3f']]`
  - `CONDITIONAL_JUMP` [`00adaf3c`](#insn-00adaf3c) → [`00adaf48`](#insn-00adaf48)
  - `FALL_THROUGH` [`00adaf3c`](#insn-00adaf3c) → [`00adaf40`](#insn-00adaf40)
- ブロック [`00adaf40`](#insn-00adaf40) 範囲 `[['00adaf40', '00adaf47']]`
  - `FALL_THROUGH` [`00adaf44`](#insn-00adaf44) → [`00adaf48`](#insn-00adaf48)
- ブロック [`00adaf48`](#insn-00adaf48) 範囲 `[['00adaf48', '00adaf57']]`
  - `CONDITIONAL_JUMP` [`00adaf54`](#insn-00adaf54) → [`00adaf94`](#insn-00adaf94)
  - `FALL_THROUGH` [`00adaf54`](#insn-00adaf54) → [`00adaf58`](#insn-00adaf58)
- ブロック [`00adaf58`](#insn-00adaf58) 範囲 `[['00adaf58', '00adaf67']]`
- ブロック [`00adaf94`](#insn-00adaf94) 範囲 `[['00adaf94', '00adaf97']]`

## 命令位置別の参照

- [`00adaedc`](#insn-00adaedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaee0`](#insn-00adaee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaef4`](#insn-00adaef4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaefc`](#insn-00adaefc) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00adaf04`](#insn-00adaf04) → `0109ff38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adaf0c`](#insn-00adaf0c) → [`00adba20`](../00adb/00adba20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adba20` · 推定シンボル `None` · 推定型 `None`
- [`00adaf1c`](#insn-00adaf1c) → [`00adaf38`](#insn-00adaf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf24`](#insn-00adaf24) → [`00adaf38`](#insn-00adaf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf38`](#insn-00adaf38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf3c`](#insn-00adaf3c) → [`00adaf48`](#insn-00adaf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf40`](#insn-00adaf40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf44`](#insn-00adaf44) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adaf4c`](#insn-00adaf4c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf54`](#insn-00adaf54) → [`00adaf94`](#insn-00adaf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf58`](#insn-00adaf58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf5c`](#insn-00adaf5c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adaf94`](#insn-00adaf94) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adaedc`](#insn-00adaedc)

~~~json
{
  "source": "00adaedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaee0`](#insn-00adaee0)

~~~json
{
  "source": "00adaee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaef4`](#insn-00adaef4)

~~~json
{
  "source": "00adaef4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaefc`](#insn-00adaefc)

~~~json
{
  "source": "00adaefc",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf04`](#insn-00adaf04)

~~~json
{
  "source": "00adaf04",
  "target": "0109ff38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109ff38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adaf0c`](#insn-00adaf0c)

~~~json
{
  "source": "00adaf0c",
  "target": "00adba20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf1c`](#insn-00adaf1c)

~~~json
{
  "source": "00adaf1c",
  "target": "00adaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf24`](#insn-00adaf24)

~~~json
{
  "source": "00adaf24",
  "target": "00adaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf38`](#insn-00adaf38)

~~~json
{
  "source": "00adaf38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf3c`](#insn-00adaf3c)

~~~json
{
  "source": "00adaf3c",
  "target": "00adaf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf40`](#insn-00adaf40)

~~~json
{
  "source": "00adaf40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf44`](#insn-00adaf44)

~~~json
{
  "source": "00adaf44",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adaf4c`](#insn-00adaf4c)

~~~json
{
  "source": "00adaf4c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf54`](#insn-00adaf54)

~~~json
{
  "source": "00adaf54",
  "target": "00adaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf58`](#insn-00adaf58)

~~~json
{
  "source": "00adaf58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf5c`](#insn-00adaf5c)

~~~json
{
  "source": "00adaf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adaf94`](#insn-00adaf94)

~~~json
{
  "source": "00adaf94",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
