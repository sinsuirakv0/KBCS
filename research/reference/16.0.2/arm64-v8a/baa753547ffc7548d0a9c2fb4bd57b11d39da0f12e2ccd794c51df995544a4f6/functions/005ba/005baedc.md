# 005baedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `005bae9c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005bae9c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0016.md#compare-fedd9cbf9366b247b5c1a9cdb754d8cf)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `005bb28c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bb/005bb28c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0023.md#compare-0010af965fdec3d600df44fb5a5d3675)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005baedc",
  "name": "FUN_005baedc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a3fc2c1a016cfee1d2d0a5f9fd7557626e5ac8b68751bbb689ec41b4e59a243",
  "source_text_sha256": "2a3fc2c1a016cfee1d2d0a5f9fd7557626e5ac8b68751bbb689ec41b4e59a243",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005baedc",
        "005baf7f"
      ],
      [
        "005bafa4",
        "005bafa7"
      ]
    ],
    "bytes_sha256": "8dc456060b87e7731bad41f485840f1ad52d3057c3d8a4343f1479cb2538a1a8",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58200](../00c58/00c58200.md)
- [00c58210](../00c58/00c58210.md)
- [00c58220](../00c58/00c58220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1344 bytes

~~~c

undefined8 FUN_005baedc(undefined8 *param_1)

{
  pthread_key_t __key;
  long lVar1;
  pthread_key_t *ppVar2;
  void *pvVar3;
  long lVar4;
  code *pcVar5;
  
  lVar1 = tpidr_el0;
  lVar4 = *(long *)(lVar1 + 0x28);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bae78 with catch @ 005baf04
                        */
  ppVar2 = (pthread_key_t *)_ZNSt6__ndk119__thread_local_dataEv();
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bae14 with catch @ 005baf08
                        */
  pvVar3 = (void *)*param_1;
  __key = *ppVar2;
  *param_1 = 0;
  pthread_setspecific(__key,pvVar3);
  pcVar5 = (code *)param_1[1];
  if ((param_1[2] & 1) != 0) {
    pcVar5 = *(code **)(pcVar5 + *(long *)(param_1[3] + ((long)param_1[2] >> 1)));
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005bafdc with catch @ 005baf30
                        */
  (*pcVar5)();
  pvVar3 = (void *)*param_1;
  *param_1 = 0;
  if (pvVar3 != (void *)0x0) {
    _ZNSt6__ndk115__thread_structD1Ev(pvVar3);
    _ZdlPv(pvVar3);
  }
  if (*(long *)(lVar1 + 0x28) == lVar4) {
                    /* try { // try from 005baf64 to 006baf7b has its CatchHandler @ 005bb00c */
    _ZdlPv(param_1);
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005baedc"></a> `005baedc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-005baee0"></a> `005baee0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005baee4"></a> `005baee4` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005baee8"></a> `005baee8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005baeec"></a> `005baeec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-005baef0"></a> `005baef0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005baef4"></a> `005baef4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005baef8"></a> `005baef8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005baefc"></a> `005baefc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005baf00"></a> `005baf00` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-005baf04"></a> `005baf04` | `bf 74 1a 94` | bl 0x00c58200 | `UNCONDITIONAL_CALL`
<a id="insn-005baf08"></a> `005baf08` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-005baf0c"></a> `005baf0c` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-005baf10"></a> `005baf10` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-005baf14"></a> `005baf14` | `bf 74 1a 94` | bl 0x00c58210 | `UNCONDITIONAL_CALL`
<a id="insn-005baf18"></a> `005baf18` | `6a 26 41 a9` | ldp x10,x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005baf1c"></a> `005baf1c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-005baf20"></a> `005baf20` | `20 05 8a 8b` | add x0,x9,x10, ASR #0x1 | `FALL_THROUGH`
<a id="insn-005baf24"></a> `005baf24` | `6a 00 00 36` | tbz w10,#0x0,0x005baf30 | `CONDITIONAL_JUMP`
<a id="insn-005baf28"></a> `005baf28` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-005baf2c"></a> `005baf2c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005baf30"></a> `005baf30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-005baf34"></a> `005baf34` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-005baf38"></a> `005baf38` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-005baf3c"></a> `005baf3c` | `b4 00 00 b4` | cbz x20,0x005baf50 | `CONDITIONAL_JUMP`
<a id="insn-005baf40"></a> `005baf40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005baf44"></a> `005baf44` | `b7 74 1a 94` | bl 0x00c58220 | `UNCONDITIONAL_CALL`
<a id="insn-005baf48"></a> `005baf48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005baf4c"></a> `005baf4c` | `0d 74 1a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-005baf50"></a> `005baf50` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005baf54"></a> `005baf54` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005baf58"></a> `005baf58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005baf5c"></a> `005baf5c` | `41 02 00 54` | b.ne 0x005bafa4 | `CONDITIONAL_JUMP`
<a id="insn-005baf60"></a> `005baf60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005baf64"></a> `005baf64` | `07 74 1a 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-005baf68"></a> `005baf68` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-005baf6c"></a> `005baf6c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005baf70"></a> `005baf70` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005baf74"></a> `005baf74` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005baf78"></a> `005baf78` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-005baf7c"></a> `005baf7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005bafa4"></a> `005bafa4` | `03 74 1a 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005baedc`](#insn-005baedc) 範囲 `[['005baedc', '005baf03']]`
  - `FALL_THROUGH` [`005baf00`](#insn-005baf00) → [`005baf04`](#insn-005baf04)
- ブロック [`005baf04`](#insn-005baf04) 範囲 `[['005baf04', '005baf07']]`
  - `FALL_THROUGH` [`005baf04`](#insn-005baf04) → [`005baf08`](#insn-005baf08)
- ブロック [`005baf08`](#insn-005baf08) 範囲 `[['005baf08', '005baf27']]`
  - `CONDITIONAL_JUMP` [`005baf24`](#insn-005baf24) → [`005baf30`](#insn-005baf30)
  - `FALL_THROUGH` [`005baf24`](#insn-005baf24) → [`005baf28`](#insn-005baf28)
- ブロック [`005baf28`](#insn-005baf28) 範囲 `[['005baf28', '005baf2f']]`
  - `FALL_THROUGH` [`005baf2c`](#insn-005baf2c) → [`005baf30`](#insn-005baf30)
- ブロック [`005baf30`](#insn-005baf30) 範囲 `[['005baf30', '005baf3f']]`
  - `CONDITIONAL_JUMP` [`005baf3c`](#insn-005baf3c) → [`005baf50`](#insn-005baf50)
  - `FALL_THROUGH` [`005baf3c`](#insn-005baf3c) → [`005baf40`](#insn-005baf40)
- ブロック [`005baf40`](#insn-005baf40) 範囲 `[['005baf40', '005baf4f']]`
  - `FALL_THROUGH` [`005baf4c`](#insn-005baf4c) → [`005baf50`](#insn-005baf50)
- ブロック [`005baf50`](#insn-005baf50) 範囲 `[['005baf50', '005baf5f']]`
  - `CONDITIONAL_JUMP` [`005baf5c`](#insn-005baf5c) → [`005bafa4`](#insn-005bafa4)
  - `FALL_THROUGH` [`005baf5c`](#insn-005baf5c) → [`005baf60`](#insn-005baf60)
- ブロック [`005baf60`](#insn-005baf60) 範囲 `[['005baf60', '005baf63']]`
  - `FALL_THROUGH` [`005baf60`](#insn-005baf60) → [`005baf64`](#insn-005baf64)
- ブロック [`005baf64`](#insn-005baf64) 範囲 `[['005baf64', '005baf7f']]`
- ブロック [`005bafa4`](#insn-005bafa4) 範囲 `[['005bafa4', '005bafa7']]`

## 命令位置別の参照

- [`005baee0`](#insn-005baee0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baee4`](#insn-005baee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baee8`](#insn-005baee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baefc`](#insn-005baefc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf00`](#insn-005baf00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf04`](#insn-005baf04) → [`00c58200`](../00c58/00c58200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58200` · 推定シンボル `None` · 推定型 `None`
- [`005baf14`](#insn-005baf14) → [`00c58210`](../00c58/00c58210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58210` · 推定シンボル `None` · 推定型 `None`
- [`005baf24`](#insn-005baf24) → [`005baf30`](#insn-005baf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf3c`](#insn-005baf3c) → [`005baf50`](#insn-005baf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf44`](#insn-005baf44) → [`00c58220`](../00c58/00c58220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58220` · 推定シンボル `None` · 推定型 `None`
- [`005baf4c`](#insn-005baf4c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`005baf54`](#insn-005baf54) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf5c`](#insn-005baf5c) → [`005bafa4`](#insn-005bafa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf64`](#insn-005baf64) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`005baf6c`](#insn-005baf6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf70`](#insn-005baf70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf74`](#insn-005baf74) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafa4`](#insn-005bafa4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005baee0`](#insn-005baee0)

~~~json
{
  "source": "005baee0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baee4`](#insn-005baee4)

~~~json
{
  "source": "005baee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baee8`](#insn-005baee8)

~~~json
{
  "source": "005baee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baefc`](#insn-005baefc)

~~~json
{
  "source": "005baefc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf00`](#insn-005baf00)

~~~json
{
  "source": "005baf00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf04`](#insn-005baf04)

~~~json
{
  "source": "005baf04",
  "target": "00c58200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf14`](#insn-005baf14)

~~~json
{
  "source": "005baf14",
  "target": "00c58210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf24`](#insn-005baf24)

~~~json
{
  "source": "005baf24",
  "target": "005baf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf3c`](#insn-005baf3c)

~~~json
{
  "source": "005baf3c",
  "target": "005baf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf44`](#insn-005baf44)

~~~json
{
  "source": "005baf44",
  "target": "00c58220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf4c`](#insn-005baf4c)

~~~json
{
  "source": "005baf4c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf54`](#insn-005baf54)

~~~json
{
  "source": "005baf54",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf5c`](#insn-005baf5c)

~~~json
{
  "source": "005baf5c",
  "target": "005bafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf64`](#insn-005baf64)

~~~json
{
  "source": "005baf64",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf6c`](#insn-005baf6c)

~~~json
{
  "source": "005baf6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf70`](#insn-005baf70)

~~~json
{
  "source": "005baf70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf74`](#insn-005baf74)

~~~json
{
  "source": "005baf74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafa4`](#insn-005bafa4)

~~~json
{
  "source": "005bafa4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
