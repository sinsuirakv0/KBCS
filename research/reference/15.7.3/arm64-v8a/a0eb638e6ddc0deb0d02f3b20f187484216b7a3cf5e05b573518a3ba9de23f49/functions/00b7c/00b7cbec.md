# 00b7cbec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b7cb24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0003.md#compare-1fab1088ccd838a91b1cde9a2219c39b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7cc30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cc30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0014.md#compare-2856bc0fc7ba1491cd82c89636d7941f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7cbec",
  "name": "_ZNSt6__ndk117__assoc_sub_state4waitEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0423d98f7f91e0350ed5ab422fda0df07355d01567184441ca12f8c65aa8b76e",
  "source_text_sha256": "0423d98f7f91e0350ed5ab422fda0df07355d01567184441ca12f8c65aa8b76e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7cbec",
        "00b7cc8f"
      ]
    ],
    "bytes_sha256": "a195e0daf978472809079beb057f8047af66d1330c1e83efcbeeefd231a37e67",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bdb690](../00bdb/00bdb690.md)

## 呼び出し先

- [00bdb240](../00bdb/00bdb240.md)
- [00bdb250](../00bdb/00bdb250.md)
- [00bdb5e0](../00bdb/00bdb5e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 929 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state4waitEv(long *param_1)

{
  long *plVar1;
  uint uVar2;
  long *local_30;
  char local_28;
  
  plVar1 = param_1 + 3;
  local_28 = '\x01';
  local_30 = plVar1;
  _ZNSt6__ndk15mutex4lockEv(plVar1);
  uVar2 = *(uint *)(param_1 + 0xe);
  if ((uVar2 >> 2 & 1) == 0) {
    if ((uVar2 >> 3 & 1) != 0) {
      *(uint *)(param_1 + 0xe) = uVar2 & 0xfffffff3;
      _ZNSt6__ndk15mutex6unlockEv(plVar1);
                    /* WARNING: Could not recover jumptable at 0x00b7cc8c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*param_1 + 0x18))(param_1);
      return;
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,&local_30);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
    if (local_28 == '\0') {
      return;
    }
  }
  _ZNSt6__ndk15mutex6unlockEv(local_30);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7cbec"></a> `00b7cbec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7cbf0"></a> `00b7cbf0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7cbf4"></a> `00b7cbf4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cbf8"></a> `00b7cbf8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7cbfc"></a> `00b7cbfc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b7cc00"></a> `00b7cc00` | `14 60 00 91` | add x20,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00b7cc04"></a> `00b7cc04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7cc08"></a> `00b7cc08` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cc0c"></a> `00b7cc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7cc10"></a> `00b7cc10` | `f4 03 00 f9` | str x20,[sp] | `FALL_THROUGH`
<a id="insn-00b7cc14"></a> `00b7cc14` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7cc18"></a> `00b7cc18` | `8a 79 01 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cc1c"></a> `00b7cc1c` | `68 72 40 b9` | ldr w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00b7cc20"></a> `00b7cc20` | `28 01 10 37` | tbnz w8,#0x2,0x00b7cc44 | `CONDITIONAL_JUMP`
<a id="insn-00b7cc24"></a> `00b7cc24` | `e8 01 18 37` | tbnz w8,#0x3,0x00b7cc60 | `CONDITIONAL_JUMP`
<a id="insn-00b7cc28"></a> `00b7cc28` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00b7cc2c"></a> `00b7cc2c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b7cc30"></a> `00b7cc30` | `6c 7a 01 94` | bl 0x00bdb5e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cc34"></a> `00b7cc34` | `68 c2 41 39` | ldrb w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00b7cc38"></a> `00b7cc38` | `88 ff 17 36` | tbz w8,#0x2,0x00b7cc28 | `CONDITIONAL_JUMP`
<a id="insn-00b7cc3c"></a> `00b7cc3c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b7cc40"></a> `00b7cc40` | `68 00 00 34` | cbz w8,0x00b7cc4c | `CONDITIONAL_JUMP`
<a id="insn-00b7cc44"></a> `00b7cc44` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b7cc48"></a> `00b7cc48` | `82 79 01 94` | bl 0x00bdb250 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cc4c"></a> `00b7cc4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7cc50"></a> `00b7cc50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cc54"></a> `00b7cc54` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7cc58"></a> `00b7cc58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7cc5c"></a> `00b7cc5c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b7cc60"></a> `00b7cc60` | `08 75 1c 12` | and w8,w8,#0xfffffff3 | `FALL_THROUGH`
<a id="insn-00b7cc64"></a> `00b7cc64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7cc68"></a> `00b7cc68` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00b7cc6c"></a> `00b7cc6c` | `79 79 01 94` | bl 0x00bdb250 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cc70"></a> `00b7cc70` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b7cc74"></a> `00b7cc74` | `10 0d 40 f9` | ldr x16,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b7cc78"></a> `00b7cc78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7cc7c"></a> `00b7cc7c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7cc80"></a> `00b7cc80` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cc84"></a> `00b7cc84` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b7cc88"></a> `00b7cc88` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7cc8c"></a> `00b7cc8c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b7cbec`](#insn-00b7cbec) 範囲 `[['00b7cbec', '00b7cc23']]`
  - `CONDITIONAL_JUMP` [`00b7cc20`](#insn-00b7cc20) → [`00b7cc44`](#insn-00b7cc44)
  - `FALL_THROUGH` [`00b7cc20`](#insn-00b7cc20) → [`00b7cc24`](#insn-00b7cc24)
- ブロック [`00b7cc24`](#insn-00b7cc24) 範囲 `[['00b7cc24', '00b7cc27']]`
  - `CONDITIONAL_JUMP` [`00b7cc24`](#insn-00b7cc24) → [`00b7cc60`](#insn-00b7cc60)
  - `FALL_THROUGH` [`00b7cc24`](#insn-00b7cc24) → [`00b7cc28`](#insn-00b7cc28)
- ブロック [`00b7cc28`](#insn-00b7cc28) 範囲 `[['00b7cc28', '00b7cc3b']]`
  - `CONDITIONAL_JUMP` [`00b7cc38`](#insn-00b7cc38) → [`00b7cc28`](#insn-00b7cc28)
  - `FALL_THROUGH` [`00b7cc38`](#insn-00b7cc38) → [`00b7cc3c`](#insn-00b7cc3c)
- ブロック [`00b7cc3c`](#insn-00b7cc3c) 範囲 `[['00b7cc3c', '00b7cc43']]`
  - `CONDITIONAL_JUMP` [`00b7cc40`](#insn-00b7cc40) → [`00b7cc4c`](#insn-00b7cc4c)
  - `FALL_THROUGH` [`00b7cc40`](#insn-00b7cc40) → [`00b7cc44`](#insn-00b7cc44)
- ブロック [`00b7cc44`](#insn-00b7cc44) 範囲 `[['00b7cc44', '00b7cc4b']]`
  - `FALL_THROUGH` [`00b7cc48`](#insn-00b7cc48) → [`00b7cc4c`](#insn-00b7cc4c)
- ブロック [`00b7cc4c`](#insn-00b7cc4c) 範囲 `[['00b7cc4c', '00b7cc5f']]`
- ブロック [`00b7cc60`](#insn-00b7cc60) 範囲 `[['00b7cc60', '00b7cc8f']]`

## 命令位置別の参照

- [`00b7cbf4`](#insn-00b7cbf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbf8`](#insn-00b7cbf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc10`](#insn-00b7cc10) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc14`](#insn-00b7cc14) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc18`](#insn-00b7cc18) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc20`](#insn-00b7cc20) → [`00b7cc44`](#insn-00b7cc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc24`](#insn-00b7cc24) → [`00b7cc60`](#insn-00b7cc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc30`](#insn-00b7cc30) → [`00bdb5e0`](../00bdb/00bdb5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb5e0` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc38`](#insn-00b7cc38) → [`00b7cc28`](#insn-00b7cc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc3c`](#insn-00b7cc3c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc40`](#insn-00b7cc40) → [`00b7cc4c`](#insn-00b7cc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc44`](#insn-00b7cc44) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc48`](#insn-00b7cc48) → [`00bdb250`](../00bdb/00bdb250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb250` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc4c`](#insn-00b7cc4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc50`](#insn-00b7cc50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc6c`](#insn-00b7cc6c) → [`00bdb250`](../00bdb/00bdb250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb250` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc7c`](#insn-00b7cc7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc80`](#insn-00b7cc80) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7cbf4`](#insn-00b7cbf4)

~~~json
{
  "source": "00b7cbf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cbf8`](#insn-00b7cbf8)

~~~json
{
  "source": "00b7cbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc10`](#insn-00b7cc10)

~~~json
{
  "source": "00b7cc10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc14`](#insn-00b7cc14)

~~~json
{
  "source": "00b7cc14",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc18`](#insn-00b7cc18)

~~~json
{
  "source": "00b7cc18",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc20`](#insn-00b7cc20)

~~~json
{
  "source": "00b7cc20",
  "target": "00b7cc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc24`](#insn-00b7cc24)

~~~json
{
  "source": "00b7cc24",
  "target": "00b7cc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc30`](#insn-00b7cc30)

~~~json
{
  "source": "00b7cc30",
  "target": "00bdb5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc38`](#insn-00b7cc38)

~~~json
{
  "source": "00b7cc38",
  "target": "00b7cc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc3c`](#insn-00b7cc3c)

~~~json
{
  "source": "00b7cc3c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc40`](#insn-00b7cc40)

~~~json
{
  "source": "00b7cc40",
  "target": "00b7cc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc44`](#insn-00b7cc44)

~~~json
{
  "source": "00b7cc44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc48`](#insn-00b7cc48)

~~~json
{
  "source": "00b7cc48",
  "target": "00bdb250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc4c`](#insn-00b7cc4c)

~~~json
{
  "source": "00b7cc4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc50`](#insn-00b7cc50)

~~~json
{
  "source": "00b7cc50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc6c`](#insn-00b7cc6c)

~~~json
{
  "source": "00b7cc6c",
  "target": "00bdb250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc7c`](#insn-00b7cc7c)

~~~json
{
  "source": "00b7cc7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc80`](#insn-00b7cc80)

~~~json
{
  "source": "00b7cc80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
